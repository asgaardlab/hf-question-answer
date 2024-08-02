from pathlib import Path

import pandas as pd
import yaml
from huggingface_hub import get_repo_discussions, get_discussion_details, Discussion, DiscussionWithDetails
from huggingface_hub.utils import RevisionNotFoundError, HfHubHTTPError

from util import path
from util.helper import get_model_dir_name


def is_saved(discussion: Discussion, save_dir: Path) -> bool:
    save_file_path = get_save_file_path(discussion, save_dir)
    return save_file_path.exists()


def download_discussion(model_id: str, save_root: Path, force_collect: bool, index: int, total: int) -> None:
    print(f'[{(index + 1)}/{total}] Downloading discussion for model {model_id}')

    save_dir = save_root / get_model_dir_name(model_id)

    if save_dir.exists() and not force_collect:
        print(' - Already downloaded. Passing to next...')
        return

    save_dir.mkdir(parents=True, exist_ok=True)

    # https://huggingface.co/docs/huggingface_hub/main/en/package_reference/community
    try:
        for discussion in get_repo_discussions(repo_id=model_id):
            print(f' - #{discussion.num} {discussion.title} {discussion.status}')

            try:
                discussion_details = get_discussion_details(repo_id=model_id, discussion_num=discussion.num)
                save_data(discussion, discussion_details, save_dir)
            except RevisionNotFoundError as e:
                save_error(discussion, e, save_dir)
    except HfHubHTTPError as e:
        save_error(None, e, save_dir)


def save_error(discussion: Discussion | None, error: Exception, save_dir: Path) -> None:
    save_file_path = get_save_file_path(discussion, save_dir, has_error=True)
    yaml.dump(discussion, save_file_path.open('w'), default_flow_style=False)
    yaml.dump(error, save_file_path.open('a'), default_flow_style=False)


def save_data(discussion: Discussion, discussion_details: DiscussionWithDetails, save_dir: Path) -> None:
    save_file_path = get_save_file_path(discussion, save_dir)
    yaml.dump(discussion_details, save_file_path.open('w'), default_flow_style=False)


def get_save_file_path(discussion: Discussion | None, save_dir: Path, has_error=False) -> Path:
    if discussion:
        if discussion.is_pull_request:
            save_file_name = 'pull_request_' + str(discussion.num)
        else:
            save_file_name = 'discussion_' + str(discussion.num)
        if has_error:
            save_file_name += '_error'
    if discussion is None and has_error:
        save_file_name = 'error'
    save_file_name += '.yaml'
    return save_dir / save_file_name


def collect_discussions_of_models(force_collect=False) -> None:
    path.DISCUSSIONS_DIRECTORY.mkdir(parents=True, exist_ok=True)
    # download_discussion('stabilityai/stable-video-diffusion-img2vid-xt', path.DISCUSSIONS_DIRECTORY)

    models = pd.read_csv(path.ALL_MODELS_FILE)
    models.apply(
        lambda model: download_discussion(model['model_id'], path.DISCUSSIONS_DIRECTORY, force_collect, model.name,
                                          len(models)), axis=1)


if __name__ == '__main__':
    collect_discussions_of_models()
