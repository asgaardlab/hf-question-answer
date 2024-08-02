from pandas import DataFrame

from data_cleaner.discussion_reader import get_selected_all_discussions, save_selected_all_discussions, \
    get_all_questions, save_all_questions
from data_cleaner.type.discussion import Discussion


def get_discussions_status(discussions) -> DataFrame:
    discussions['status'] = discussions['discussion_path'].apply(
        lambda discussion_path: Discussion.from_path_str(discussion_path).get_status())
    return discussions


def get_discussions_status_change_count(discussions) -> DataFrame:
    discussions['status_change_count'] = discussions['discussion_path'].apply(
        lambda discussion_path: Discussion.from_path_str(discussion_path).get_status_changes_count())
    return discussions


if __name__ == '__main__':
    all_discussions = get_all_questions()

    all_discussions = get_discussions_status(all_discussions)
    all_discussions = get_discussions_status_change_count(all_discussions)

    save_all_questions(all_discussions)
