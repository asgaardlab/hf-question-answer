import pickle

import pandas as pd
from pandas import DataFrame

from data_collector.type.discussion import Discussion
from util import path
from util.helper import save_data_in_filepath


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


def save_all_discussions(dataset: DataFrame) -> None:
    dataset.to_csv(path.ALL_DISCUSSIONS_FILE, index=False)


def get_cleaned_all_discussions() -> DataFrame:
    if path.CLEANED_DISCUSSIONS_FILE.exists():
        return pd.read_csv(path.CLEANED_DISCUSSIONS_FILE)


def save_cleaned_all_discussions(dataset: DataFrame = None) -> None:
    if dataset is None:
        get_cleaned_all_discussions()
    else:
        dataset.to_csv(path.CLEANED_DISCUSSIONS_FILE, index=False)


def get_all_random_discussions() -> DataFrame:
    return pd.read_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, na_values='$@$', keep_default_na=False)


def save_all_random_discussions(dataset: DataFrame) -> None:
    dataset.to_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, index=False)


def get_cleaned_random_discussions() -> DataFrame:
    if path.CLEANED_RANDOM_DISCUSSIONS_FILE.exists():
        return pd.read_csv(path.CLEANED_RANDOM_DISCUSSIONS_FILE)

    random_discussions = get_all_random_discussions()
    hidden_filtered_discussions = random_discussions[random_discussions['is_hidden'] == False]
    length_filtered_discussions = hidden_filtered_discussions[hidden_filtered_discussions['length'] >= 50]
    language_filtered_discussions = length_filtered_discussions[length_filtered_discussions['is_non_english'] == False]
    save_cleaned_random_discussions(language_filtered_discussions)
    return language_filtered_discussions


def save_cleaned_random_discussions(dataset: DataFrame = None):
    if dataset is None:
        get_cleaned_random_discussions()
    else:
        dataset.to_csv(path.CLEANED_RANDOM_DISCUSSIONS_FILE, index=False)


def get_all_questions() -> DataFrame:
    if path.ALL_QUESTIONS_FILE.exists():
        return pd.read_csv(path.ALL_QUESTIONS_FILE)
    else:
        discussions = get_cleaned_all_discussions()
        questions = discussions[discussions['contains_question_final_class'] == 'yes']
        questions.to_csv(path.ALL_QUESTIONS_FILE, index=False)
        return questions


def save_all_questions(dataset: DataFrame = None) -> None:
    if dataset is None:
        get_all_questions()
    else:
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
