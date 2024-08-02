import pickle
import re
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from progress.bar import IncrementalBar

from data_cleaner.type.discussion import Discussion
from util import path
from util.helper import save_data_in_filepath


def get_discussion_paths_from_cache() -> list[Path]:
    if path.DISCUSSION_FILE_PATHS_CACHE.exists():
        with path.DISCUSSION_FILE_PATHS_CACHE.open('rb') as file:
            discussion_paths = pickle.load(file)
    else:
        discussion_paths = [file_path for file_path in path.DISCUSSIONS_DIRECTORY.glob('*/*.yaml') if
                            file_path.name.startswith('discussion_')]
        save_data_in_filepath(discussion_paths, path.DISCUSSION_FILE_PATHS_CACHE)
    return discussion_paths


def get_discussion_url(discussion_path: str) -> str:
    discussion = Discussion.from_path_str(discussion_path)
    return discussion.url


def get_all_discussions() -> DataFrame:
    if path.ALL_DISCUSSIONS_FILE.exists():
        return pd.read_csv(path.ALL_DISCUSSIONS_FILE)
    else:
        print('Creating discussions file')
        discussion_paths = [file_path for file_path in path.DISCUSSIONS_DIRECTORY.glob('*/*.yaml') if
                            file_path.name.startswith('discussion_')]
        discussion_paths_df = pd.DataFrame(
            {'discussion_path': [str(discussion_path) for discussion_path in discussion_paths]})
        discussion_paths_df['discussion_url'] = discussion_paths_df['discussion_path'].apply(get_discussion_url)
        discussion_paths_df.index.name = 'index'
        discussion_paths_df.to_csv(path.ALL_DISCUSSIONS_FILE, index=True)
        return discussion_paths_df


def get_selected_all_discussions() -> DataFrame:
    if path.SELECTED_ALL_DISCUSSIONS_FILE.exists():
        return pd.read_csv(path.SELECTED_ALL_DISCUSSIONS_FILE)

    all_discussions = get_all_discussions()
    hidden_filtered_discussions = all_discussions[all_discussions['is_hidden'] == False]
    length_filtered_discussions = hidden_filtered_discussions[hidden_filtered_discussions['length'] >= 50]
    language_filtered_discussions = length_filtered_discussions[length_filtered_discussions['is_non_english'] == False]
    save_selected_all_discussions(language_filtered_discussions)
    return language_filtered_discussions


def save_selected_all_discussions(dataset: DataFrame = None) -> None:
    if dataset is None:
        get_selected_all_discussions()
    else:
        dataset.to_csv(path.SELECTED_ALL_DISCUSSIONS_FILE, index=False)


def get_posts_of_selected_discussions() -> list[str]:
    if path.DISCUSSION_POSTS_FILE.exists():
        with path.DISCUSSION_POSTS_FILE.open('rb') as file:
            return pickle.load(file)
    else:
        selected_discussions = get_selected_all_discussions()
        selected_discussions['post'] = selected_discussions['discussion_path'].apply(
            lambda discussion_path: Discussion.from_path_str(discussion_path).get_post())
        posts = selected_discussions['index', 'post'].values.tolist()
        save_data_in_filepath(posts, path.DISCUSSION_POSTS_FILE)
        return posts


def get_posts_of_random_discussions() -> dict[int, str]:
    if path.RANDOM_DISCUSSION_POSTS_FILE.exists():
        with path.RANDOM_DISCUSSION_POSTS_FILE.open('rb') as file:
            return pickle.load(file)
    else:
        random_discussions = get_all_random_discussions()
        random_discussions['post'] = random_discussions['discussion_path'].apply(
            lambda discussion_path: Discussion.from_path_str(discussion_path).get_post())
        posts = dict(zip(random_discussions['index'], random_discussions['post']))
        save_data_in_filepath(posts, path.RANDOM_DISCUSSION_POSTS_FILE)
        return posts


def save_all_discussions(dataset: DataFrame) -> None:
    dataset.to_csv(path.ALL_DISCUSSIONS_FILE, index=False)


def get_all_random_discussions() -> DataFrame:
    return pd.read_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, na_values='$@$', keep_default_na=False)


def get_selected_random_discussions() -> DataFrame:
    if path.SELECTED_RANDOM_DISCUSSIONS_FILE.exists():
        return pd.read_csv(path.SELECTED_RANDOM_DISCUSSIONS_FILE)

    random_discussions = get_all_random_discussions()
    hidden_filtered_discussions = random_discussions[random_discussions['is_hidden'] == False]
    length_filtered_discussions = hidden_filtered_discussions[hidden_filtered_discussions['length'] >= 50]
    language_filtered_discussions = length_filtered_discussions[length_filtered_discussions['is_non_english'] == False]
    save_selected_random_discussions(language_filtered_discussions)
    return language_filtered_discussions


def save_selected_random_discussions(dataset: DataFrame = None):
    if dataset is None:
        get_selected_random_discussions()
    else:
        dataset.to_csv(path.SELECTED_RANDOM_DISCUSSIONS_FILE, index=False)


def get_random_discussion_paths() -> list[str]:
    discussions = pd.read_csv(path.ALL_RANDOM_DISCUSSIONS_FILE)
    return discussions['discussion_path'].values.tolist()


def save_all_random_discussions(dataset: DataFrame) -> None:
    dataset.to_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, index=False)


def get_discussions(reload=False) -> list[Discussion]:
    if path.DISCUSSIONS_CACHE.exists() and not reload:
        with path.DISCUSSIONS_CACHE.open('rb') as file:
            discussions = pickle.load(file)
    else:
        discussion_paths = get_all_discussions()['discussion_path'].tolist()

        discussions = []
        with IncrementalBar('Reading discussions', max=len(discussion_paths)) as bar:
            for discussion_path in discussion_paths:
                discussion = Discussion.from_path_str(discussion_path)
                discussions.append(discussion)
                bar.next()
        save_data_in_filepath(discussions, path.DISCUSSIONS_CACHE)

    return discussions


def get_discussions_df() -> DataFrame:
    discussions = get_discussions()
    discussions_df = pd.DataFrame([discussion.__dict__ for discussion in discussions])

    return discussions_df


def get_all_questions() -> DataFrame:
    if path.ALL_QUESTIONS_FILE.exists():
        return pd.read_csv(path.ALL_QUESTIONS_FILE)
    else:
        discussions = get_selected_all_discussions()
        questions = discussions[discussions['contains_question_final_class'] == 'yes']
        questions.to_csv(path.ALL_QUESTIONS_FILE, index=False)
        return questions


def get_quality_questions() -> DataFrame:
    return pd.read_csv(path.QUALITY_MODELS_QUESTIONS_FILE)


def save_quality_questions(dataset: DataFrame) -> None:
    dataset.to_csv(path.QUALITY_MODELS_QUESTIONS_FILE, index=False)


def save_all_questions(dataset: DataFrame) -> None:
    dataset.to_csv(path.ALL_QUESTIONS_FILE, index=False)


def get_posts_of_all_questions() -> list[str]:
    if path.ALL_QUESTION_POSTS_FILE.exists():
        with path.ALL_QUESTION_POSTS_FILE.open('rb') as file:
            return pickle.load(file)
    else:
        all_questions = get_all_questions()
        all_questions['post'] = all_questions['discussion_path'].apply(
            lambda discussion_path: Discussion.from_path_str(discussion_path).get_post())
        posts = all_questions['post'].values.tolist()
        save_data_in_filepath(posts, path.ALL_QUESTION_POSTS_FILE)
        return posts


def get_discussion_path_from_url(url: str) -> str:
    discussions = get_all_discussions()
    return discussions[discussions['discussion_url'] == url]['discussion_path'].values[0]



if __name__ == '__main__':
    # read_discussions()
    # read_discussions_without_code_block()
    # get_discussions_df()
    # save_selected_random_discussions()
    save_selected_all_discussions()