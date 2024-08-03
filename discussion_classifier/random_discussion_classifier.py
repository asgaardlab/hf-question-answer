from pathlib import Path

from pandas import DataFrame

from data_cleaner.discussion_reader import get_cleaned_random_discussions, save_cleaned_random_discussions
from discussion_classifier.classification_result_reader_writer import get_gpt_classes, get_final_class
from discussion_classifier.gpt_classifier import classify_discussions
from discussion_classifier.statistics_provider import provide_randon_discussion_classification_statistics
from util import path


def write_gpt_classes_of_random_discussions(discussions: DataFrame, result_directory: Path, write_column_name: str):
    discussions = get_gpt_classes(discussions, result_directory, write_column_name)
    save_cleaned_random_discussions(discussions)


def write_final_class():
    random_discussions = get_cleaned_random_discussions()
    random_discussions['contains_question_final_class'] = random_discussions.apply(
        lambda discussion: get_final_class(discussion, 'contains_question_run_3'), axis=1)
    save_cleaned_random_discussions(random_discussions)


if __name__ == '__main__':
    cleaned_random_discussions = get_cleaned_random_discussions()

    run_result_directory = path.RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY / 'run_1'
    classify_discussions(cleaned_random_discussions, run_result_directory)
    write_gpt_classes_of_random_discussions(cleaned_random_discussions, run_result_directory,
                                            'contains_question_run_1')

    run_result_directory = path.RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY / 'run_2'
    classify_discussions(cleaned_random_discussions, run_result_directory)
    write_gpt_classes_of_random_discussions(cleaned_random_discussions, run_result_directory,
                                            'contains_question_run_2')

    run_result_directory = path.RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY / 'run_3'
    classify_discussions(cleaned_random_discussions, run_result_directory)
    write_gpt_classes_of_random_discussions(cleaned_random_discussions, run_result_directory,
                                            'contains_question_run_3')

    write_final_class()
    provide_randon_discussion_classification_statistics()
