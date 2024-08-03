from data_cleaner.discussion_reader import get_all_discussions
from util import path


def select_random_discussions(number_of_discussions_to_select: int) -> None:
    all_discussions = get_all_discussions()
    print(f'Selecting {number_of_discussions_to_select} random discussions from {len(all_discussions)} discussions')

    all_discussions.sample(number_of_discussions_to_select).to_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, index=False)


if __name__ == '__main__':
    select_random_discussions(378)
    