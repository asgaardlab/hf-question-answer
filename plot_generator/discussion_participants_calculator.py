from pandas import DataFrame

from data_cleaner.discussion_reader import get_cleaned_all_discussions, save_cleaned_all_discussions
from data_collector.type.discussion import Discussion


def calculate_discussions_participants(discussions) -> DataFrame:
    discussions['no_of_participants'] = discussions['discussion_path'].apply(
        lambda discussion_path: len(Discussion.from_path_str(discussion_path).get_participants()))
    return discussions


if __name__ == '__main__':
    all_discussions = get_cleaned_all_discussions()

    all_discussions = calculate_discussions_participants(all_discussions)
    save_cleaned_all_discussions(all_discussions)
