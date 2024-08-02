from pathlib import Path

from pandas import DataFrame

from data_cleaner.discussion_reader import get_selected_all_discussions, save_selected_all_discussions, \
    save_all_questions
from discussion_classifier.classification_result_reader_writer import get_gpt_classes, \
    get_final_class, read_class_from_result_file
from discussion_classifier.gpt_classifier import classify_discussions
from util import path


def write_gpt_classes_of_all_discussions(discussions, result_directory, write_column_name: str):
    discussions = get_gpt_classes(discussions, result_directory, write_column_name)
    save_selected_all_discussions(discussions)


def get_ties(discussions) -> DataFrame:
    ties = discussions[discussions['contains_question_run_1'] != discussions['contains_question_run_2']]

    return ties[ties['contains_question_run_1'] != 'error']


def break_ties(save_directory: Path) -> list:
    selected_all_discussions = get_selected_all_discussions()

    ties = get_ties(selected_all_discussions)
    print(f'Breaking ties for {len(ties)} discussions')

    tied_discussions = selected_all_discussions[selected_all_discussions['index'].isin(ties['index'].values)]
    classify_discussions(tied_discussions, save_directory)

    return ties['index'].values


def write_final_class():
    selected_all_discussions = get_selected_all_discussions()
    selected_all_discussions['contains_question_final_class'] = selected_all_discussions.apply(
        lambda discussion: get_final_class(discussion, 'contains_question_tie_breaker'), axis=1)
    save_selected_all_discussions(selected_all_discussions)


def write_tie_breaker_class(result_directory, indexes_to_write, write_column_name: str):
    discussions = get_selected_all_discussions()
    result_files = result_directory.glob('*_result_gpt-3-5.md')

    contains_questions = {}
    for result_file in result_files:
        discussion_index = int(result_file.name.split('_')[0])
        contains_question = read_class_from_result_file(result_directory / result_file)
        contains_questions[discussion_index] = contains_question

    discussions_having_no_result_files = discussions[~discussions['index'].isin(indexes_to_write)]

    for index in discussions_having_no_result_files['index'].values:
        contains_questions[index] = 'error'

    discussions[write_column_name] = discussions['index'].map(contains_questions)
    save_selected_all_discussions(discussions)


if __name__ == '__main__':
    selected_all_discussions = get_selected_all_discussions()

    run_result_directory = path.ALL_DISCUSSION_CLASSIFICATION_DIRECTORY / 'run1'
    classify_discussions(selected_all_discussions, run_result_directory)
    write_gpt_classes_of_all_discussions(selected_all_discussions, run_result_directory,
                                         'contains_question_run_1')

    run_result_directory = path.ALL_DISCUSSION_CLASSIFICATION_DIRECTORY / 'run2'
    classify_discussions(selected_all_discussions, run_result_directory)
    write_gpt_classes_of_all_discussions(selected_all_discussions, run_result_directory, 'contains_question_run_2')

    run_result_directory = path.RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY / 'tie_breakers'
    tie_indexes = break_ties(run_result_directory)
    write_tie_breaker_class(run_result_directory, tie_indexes, 'contains_question_tie_breaker')

    write_final_class()
    save_all_questions()
