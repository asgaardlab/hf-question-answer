from pandas import DataFrame

from data_cleaner.discussion_reader import get_selected_all_discussions, save_selected_all_discussions, \
    get_all_questions, save_all_questions
from data_cleaner.type.discussion import Discussion


def calculate_discussions_responses(discussions) -> DataFrame:
    discussions['no_of_responses'] = discussions['discussion_path'].apply(
        lambda discussion_path: len(Discussion.from_path_str(discussion_path).get_responses()))
    return discussions


def calculate_has_owner_responses(discussions) -> DataFrame:
    discussions['has_owner_responses'] = discussions['discussion_path'].apply(
        lambda discussion_path: Discussion.from_path_str(discussion_path).has_owner_response())
    return discussions


def calculate_discussions_contributors_responses(discussions) -> DataFrame:
    discussions['no_of_contributor_responses'] = discussions['discussion_path'].apply(
        lambda discussion_path: len(Discussion.from_path_str(discussion_path).get_contributor_responses()))
    return discussions


def get_responses_word_lengths(discussion_path: str) -> int:
    responses = Discussion.from_path_str(discussion_path).get_responses()
    print(responses)
    responses_word_lengths = [len(response.split()) for response in responses]

    return sum(responses_word_lengths)


def calculate_response_length(discussions: DataFrame) -> DataFrame:
    discussions['responses_length_per_word_count'] = discussions['discussion_path'].apply(
        lambda discussion_path: get_responses_word_lengths(discussion_path))

    return discussions


if __name__ == '__main__':
    all_discussions = get_all_questions()

    all_discussions = calculate_discussions_responses(all_discussions)
    all_discussions = calculate_discussions_contributors_responses(all_discussions)
    all_discussions = calculate_has_owner_responses(all_discussions)
    all_discussions = calculate_response_length(all_discussions)

    save_all_questions(all_discussions)
