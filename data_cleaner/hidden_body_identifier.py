from pandas import DataFrame

from data_cleaner.discussion_reader import get_all_discussions, save_all_discussions, get_all_random_discussions, \
    save_all_random_discussions
from data_collector.type.discussion import Discussion


def is_body_hidden(discussion_path: str) -> bool:
    discussion = Discussion.from_path_str(discussion_path)
    return discussion.is_hidden


def identify_hidden_discussions(discussions: DataFrame) -> DataFrame:
    discussions = discussions.drop(['is_hidden'], axis=1, errors='ignore')

    print('Identifying hidden discussions')
    discussions['is_hidden'] = discussions['discussion_path'].apply(is_body_hidden)
    return discussions


def save_random_hidden_discussions() -> DataFrame:
    random_discussions = get_all_random_discussions()
    random_discussions = identify_hidden_discussions(random_discussions)
    save_all_random_discussions(random_discussions)

    return random_discussions


def save_all_hidden_discussions() -> DataFrame:
    all_discussions = get_all_discussions()
    all_discussions = identify_hidden_discussions(all_discussions)
    save_all_discussions(all_discussions)

    return all_discussions


if __name__ == '__main__':
    save_random_hidden_discussions()
    save_all_hidden_discussions()

