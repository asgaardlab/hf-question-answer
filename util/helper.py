import pickle
from pathlib import Path

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


def get_discussion_path(discussion_url: str) -> Path:
    url_parts = discussion_url.split('/')
    discussion_number = url_parts[-1]
    model_id = url_parts[-4] + '/' + url_parts[-3]
    model_dir_name = get_model_dir_name(model_id)
    return path.DISCUSSIONS_DIRECTORY / model_dir_name / f'discussion_{discussion_number}.yaml'
