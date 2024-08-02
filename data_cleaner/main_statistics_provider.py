import pandas as pd
from pandas import DataFrame

from util import path


def provide_discussion_filtering_statistics(discussions: DataFrame) -> None:
    print(f'Total discussions before cleaning: {len(discussions)}')

    hidden_filtered_discussions = discussions[discussions['is_hidden'] == False]
    print(f'Total discussions after removing hidden body: {len(hidden_filtered_discussions)}')

    length_filtered_discussions = hidden_filtered_discussions[hidden_filtered_discussions['length'] >= 50]
    print(f'Total discussions after removing short discussions: {len(length_filtered_discussions)}')

    language_filtered_discussions = length_filtered_discussions[length_filtered_discussions['is_non_english'] == False]
    print(f'Total discussions after removing non-English discussions: {len(language_filtered_discussions)}')


def data_cleaning_statistics() -> None:
    all_models = pd.read_csv(path.ALL_MODELS_FILE)
    print(f'All models: {len(all_models)}')

    quality_models = pd.read_csv(path.QUALITY_MODELS_FILE)
    print(f'Quality models: {len(quality_models)}')

    all_discussions = pd.read_csv(path.ALL_DISCUSSIONS_FILE)
    print(f'All discussions: {len(all_discussions)}')

    quality_models_discussions = pd.read_csv(path.QUALITY_MODELS_DISCUSSIONS_FILE)
    print(f'Quality models discussions: {len(quality_models_discussions)}')

    cleaned_discussions = pd.read_csv(path.SELECTED_QUALITY_MODELS_DISCUSSIONS_FILE)
    print(f'Cleaned discussions: {len(cleaned_discussions)}')

    print('Cleaning step by step:')
    provide_discussion_filtering_statistics(quality_models_discussions)


if __name__ == '__main__':
    data_cleaning_statistics()
