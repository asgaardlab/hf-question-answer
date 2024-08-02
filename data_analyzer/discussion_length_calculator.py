from pandas import DataFrame

from data_cleaner.discussion_reader import get_all_random_discussions, save_all_random_discussions, \
    get_all_discussions, save_all_discussions
from data_analyzer.md_processor import remove_report_emoji, remove_urls_from_images
from data_analyzer.md_processor import remove_urls_from_hyperlinks, remove_urls
from data_cleaner.type.discussion import Discussion


def calculate_discussion_length(discussion_path: str) -> int:
    full_discussion = Discussion.from_path_str(discussion_path).get_full_discussion()

    full_discussion = remove_report_emoji(full_discussion)
    full_discussion = remove_urls_from_images(full_discussion)
    full_discussion = remove_urls_from_hyperlinks(full_discussion)
    full_discussion = remove_urls(full_discussion)

    return len(full_discussion.strip())


def calculate_discussion_lengths(discussions: DataFrame) -> DataFrame:
    print('Calculating discussion lengths')
    discussions = discussions.drop(['length'], axis=1, errors='ignore')

    discussions['length'] = discussions.apply(
        lambda discussion: calculate_discussion_length(discussion['discussion_path']), axis=1)

    return discussions


def calculate_random_discussion_lengths() -> DataFrame:
    random_discussions = get_all_random_discussions()
    random_discussions = calculate_discussion_lengths(random_discussions)
    save_all_random_discussions(random_discussions)
    return random_discussions


def calculate_all_discussion_lengths() -> DataFrame:
    all_discussions = get_all_discussions()
    all_discussions = calculate_discussion_lengths(all_discussions)
    save_all_discussions(all_discussions)
    return all_discussions


if __name__ == '__main__':
    calculate_random_discussion_lengths()
    calculate_all_discussion_lengths()
    # discussion_path = path.DISCUSSIONS_DIRECTORY / 'mosaicml@mpt-7b\discussion_28.yaml'
    # print(calculate_discussion_length(discussion_path))
