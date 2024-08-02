from datetime import timedelta

from pandas import DataFrame, Series

from data_cleaner.discussion_reader import get_selected_all_discussions, save_selected_all_discussions
from data_collector.type.discussion import Discussion


def calculate_discussions_creation_time(discussions) -> DataFrame:
    discussions['discussion_created_at'] = discussions['discussion_path'].apply(
        lambda discussion_path: Discussion.from_path_str(discussion_path).created_at)
    return discussions


def calculate_discussion_response_delay(discussion_row: Series) -> timedelta | None:
    discussion = Discussion.from_path_str(discussion_row['discussion_path'])
    response_delay = discussion.get_first_response_delay()
    return response_delay


def calculate_discussions_response_delay(discussions) -> DataFrame:
    discussions['discussion_response_delay'] = discussions.apply(
        lambda discussion: calculate_discussion_response_delay(discussion), axis=1)
    return discussions


if __name__ == '__main__':
    all_discussions = get_selected_all_discussions()

    all_discussions = calculate_discussions_creation_time(all_discussions)
    all_discussions = calculate_discussions_response_delay(all_discussions)

    save_selected_all_discussions(all_discussions)
