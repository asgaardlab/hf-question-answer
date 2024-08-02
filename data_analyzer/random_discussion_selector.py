from data_cleaner.discussion_reader import get_all_discussions
from util import path


def select_random_discussions():
    all_discussions = get_all_discussions()
    all_discussions.index = all_discussions.reset_index().index + 1
    all_discussions.index.name = 'order'
    all_discussions.sample(378).to_csv(path.ALL_RANDOM_DISCUSSIONS_FILE, index=True)


if __name__ == '__main__':
    select_random_discussions()
    