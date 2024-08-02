from pathlib import Path

import pandas as pd

from data_analyzer.discussion_length_calculator import calculate_all_discussion_lengths
from data_cleaner.discussion_reader import get_all_discussions
from data_cleaner.hidden_body_identifier import save_all_hidden_discussions
from data_cleaner.main_statistics_provider import data_cleaning_statistics
from data_cleaner.non_english_identifier import save_all_non_english_discussions
from util import path


def save_quality_models(save_file_name: Path):
    models = pd.read_csv(path.ALL_MODELS_FILE)
    print(f'All models: {len(models)}')
    quality_models = models[(models['likes'] >= 1) & (models['downloads'] >= 1)]
    print(f'quality_models: {len(quality_models)}')
    quality_models.to_csv(save_file_name, index=False)


def save_all_discussions_of_quality_models(save_file_name: Path):
    quality_models = pd.read_csv(path.QUALITY_MODELS_FILE)
    discussions = get_all_discussions()
    print(f'All discussions: {len(discussions)}')
    quality_models_discussions = discussions[discussions['model_id'].isin(quality_models['model_id'])]
    print(f'quality_models_discussions: {len(quality_models_discussions)}')
    quality_models_discussions.to_csv(save_file_name, index=False)


def save_cleaned_discussions(save_file_name: Path):
    quality_models_discussions = pd.read_csv(path.QUALITY_MODELS_DISCUSSIONS_FILE)

    hidden_filtered_discussions = quality_models_discussions[quality_models_discussions['is_hidden'] == False]
    length_filtered_discussions = hidden_filtered_discussions[hidden_filtered_discussions['length'] >= 50]
    language_filtered_discussions = length_filtered_discussions[length_filtered_discussions['is_non_english'] == False]

    print(f'cleaned_discussions: {len(language_filtered_discussions)}')
    language_filtered_discussions.to_csv(save_file_name, index=False)


if __name__ == '__main__':
    save_quality_models(path.QUALITY_MODELS_FILE)

    save_all_hidden_discussions()
    save_all_non_english_discussions()
    calculate_all_discussion_lengths()

    save_all_discussions_of_quality_models(path.QUALITY_MODELS_DISCUSSIONS_FILE)
    save_cleaned_discussions(path.SELECTED_QUALITY_MODELS_DISCUSSIONS_FILE)

    data_cleaning_statistics()

