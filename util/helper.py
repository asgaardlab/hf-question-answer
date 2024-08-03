import pickle
from pathlib import Path

import pandas as pd

from data_collector.type.discussion import Discussion
from util import path


def get_model_dir_name(model_id):
    dir_name = model_id.replace('/', '@')
    if dir_name[-1] == ".":
        dir_name = dir_name[:-1] + "$"
    return dir_name


def save_data_in_filepath(data: list | dict, file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('wb') as file:
        pickle.dump(data, file)


def get_discussion_url(discussion_path: str) -> str:
    discussion = Discussion.from_path_str(discussion_path)
    return discussion.url


def get_model_id_from_discussion_url(discussion_url: str) -> str:
    url_parts = discussion_url.split('/')
    if len(url_parts) == 6:
        return url_parts[3]
    return url_parts[3] + '/' + url_parts[4]


def list_discussions():
    print('Listing discussions...')
    discussion_paths = [file_path for file_path in path.DISCUSSIONS_DIRECTORY.glob('*/*.yaml') if
                        file_path.name.startswith('discussion_')]
    discussion_paths_df = pd.DataFrame(
        {'discussion_path': [str(discussion_path.relative_to(path.DISCUSSIONS_DIRECTORY)) for discussion_path in discussion_paths]})
    discussion_paths_df['discussion_url'] = discussion_paths_df['discussion_path'].apply(get_discussion_url)
    discussion_paths_df['model_id'] = discussion_paths_df['discussion_url'].apply(get_model_id_from_discussion_url)
    discussion_paths_df.index.name = 'index'
    discussion_paths_df.to_csv(path.ALL_DISCUSSIONS_FILE, index=True)
