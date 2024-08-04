from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


DATA_DIRECTORY = get_project_root() / 'data_to_upload'

BERTOPIC_MODEL_DIRECTORY = DATA_DIRECTORY / 'bertopic_model'
BERTOPIC_MODEL_FILE = BERTOPIC_MODEL_DIRECTORY / 'model_min_cluster_size_60'
CUSTOM_LABELS_FILE = BERTOPIC_MODEL_DIRECTORY / 'topic_custom_label.csv'

CACHE_DIRECTORY = DATA_DIRECTORY / 'cache'
QUESTION_POSTS_FILE = CACHE_DIRECTORY / 'question_posts.pkl'

CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications'
SYSTEM_PROMPT_FILE = CLASSIFICATION_DIRECTORY / 'system_prompt.md'
RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY = CLASSIFICATION_DIRECTORY / 'random_discussion_classification'
ALL_DISCUSSION_CLASSIFICATION_DIRECTORY = CLASSIFICATION_DIRECTORY / 'all_discussion_classification'

DISCUSSIONS_DIRECTORY = DATA_DIRECTORY / 'discussions'
PLOTS_DIRECTORY = DATA_DIRECTORY / 'plots'

ALL_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_discussions.csv'
ALL_MODELS_FILE = DATA_DIRECTORY / 'all_models.csv'
ALL_QUESTIONS_FILE = DATA_DIRECTORY / 'all_questions.csv'
ALL_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_random_discussions.csv'
CLEANED_DISCUSSIONS_FILE = DATA_DIRECTORY / 'cleaned_discussions.csv'
CLEANED_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'cleaned_random_discussions.csv'
QUALITY_MODELS_FILE = DATA_DIRECTORY / 'quality_models.csv'
QUALITY_MODELS_DISCUSSIONS_FILE = DATA_DIRECTORY / 'quality_models_discussions.csv'
