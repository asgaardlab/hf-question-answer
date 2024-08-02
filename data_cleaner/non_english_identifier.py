from pandas import DataFrame
from transformers import Pipeline, pipeline

from data_cleaner.discussion_reader import get_all_random_discussions, save_all_random_discussions, \
    get_all_discussions, save_all_discussions
from data_analyzer.md_processor import remove_report_emoji, remove_urls_from_images, remove_urls_from_hyperlinks, \
    remove_urls
from data_collector.type.discussion import Discussion


def is_non_english(discussion_path: str, pipe: Pipeline) -> bool:
    full_discussion = Discussion.from_path_str(discussion_path).get_full_discussion()
    # print(full_discussion)

    full_discussion = remove_report_emoji(full_discussion)
    full_discussion = remove_urls_from_images(full_discussion)
    full_discussion = remove_urls_from_hyperlinks(full_discussion)
    full_discussion = remove_urls(full_discussion)
    full_discussion = full_discussion.strip()
    # print(full_discussion)

    predictions = pipe(full_discussion, top_k=2, truncation=True)
    # print(predictions)
    return 'en' != predictions[0]['label']


def identify_non_english_discussions(discussions: DataFrame) -> DataFrame:
    discussions = discussions.drop(['is_non_english'], axis=1, errors='ignore')

    print('Identifying non-English discussions')
    model_ckpt = 'papluca/xlm-roberta-base-language-detection'
    pipe = pipeline('text-classification', model=model_ckpt)

    discussions['is_non_english'] = discussions['discussion_path'].apply(
        lambda discussion_path: is_non_english(discussion_path, pipe))

    return discussions


def save_random_non_english_discussions() -> DataFrame:
    random_discussions = get_all_random_discussions()
    random_discussions = identify_non_english_discussions(random_discussions)
    save_all_random_discussions(random_discussions)

    return random_discussions


def save_all_non_english_discussions() -> DataFrame:
    all_discussions = get_all_discussions()
    all_discussions = identify_non_english_discussions(all_discussions)
    save_all_discussions(all_discussions)

    return all_discussions


if __name__ == '__main__':
    save_random_non_english_discussions()
    save_all_non_english_discussions()
