from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


DATA_DIRECTORY = get_project_root() / 'data'
ALL_MODELS_FILE = DATA_DIRECTORY / 'all_models.csv'

DISCUSSIONS_DIRECTORY = DATA_DIRECTORY / 'discussions'
# DISCUSSION_FILE_PATHS_CACHE = CACHE_DIRECTORY / 'discussion_file_paths.pkl'
# DISCUSSIONS_CACHE = CACHE_DIRECTORY / 'discussions.pkl'
# PREPROCESSED_DISCUSSIONS_FILE = CACHE_DIRECTORY / 'preprocessed_discussions.csv'
# CLASSIFIED_DISCUSSIONS_FILE = DATA_DIRECTORY / 'classified_discussions.csv'

PLOTS_DIRECTORY = DATA_DIRECTORY / 'plots'

# PROMPTS_AND_RESULTS_DIRECTORY = DATA_DIRECTORY / 'prompts_and_results'
# UPDATED_PROMPT_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '3. updated_prompt'
# CLASSIFICATION_WITH_DESCRIPTION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '4. classification_with_class_description'
# BINARY_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '5. binary_classification'
# QUESTION_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '6. question_classification' / 'run_10'
#
CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications'
SYSTEM_PROMPT_FILE = CLASSIFICATION_DIRECTORY / 'system_prompt.md'
RANDOM_DISCUSSION_CLASSIFICATION_DIRECTORY = CLASSIFICATION_DIRECTORY / 'random_discussion_classification'
ALL_DISCUSSION_CLASSIFICATION_DIRECTORY = CLASSIFICATION_DIRECTORY / 'all_discussion_classification'

ALL_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_discussions.csv'
ALL_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_random_discussions.csv'
#
# DISCUSSION_POSTS_FILE = CACHE_DIRECTORY / 'discussion_posts.pkl'
# RANDOM_DISCUSSION_POSTS_FILE = CACHE_DIRECTORY / 'random_discussion_posts.pkl'
# ALL_QUESTION_POSTS_FILE = CACHE_DIRECTORY / 'all_question_posts.pkl'
CACHE_DIRECTORY = DATA_DIRECTORY / 'cache'
QUESTION_POSTS_FILE = CACHE_DIRECTORY / 'question_posts.pkl'
#
CLEANED_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'cleaned_random_discussions.csv'
# SELECTED_ALL_DISCUSSIONS_FILE = DATA_DIRECTORY / 'selected_all_discussions.csv'
ALL_QUESTIONS_FILE = DATA_DIRECTORY / 'all_questions.csv'
#
# TOPICS_DIRECTORY = DATA_DIRECTORY / 'topics' / 'train_v10'
#
# PREPROCESSED_POSTS_CACHE = CACHE_DIRECTORY / 'preprocessed_posts.pkl'
#
# QUALITY_FILTERED_DIRECTORY = DATA_DIRECTORY / 'quality_filtered'
QUALITY_MODELS_FILE = DATA_DIRECTORY / 'quality_models.csv'
QUALITY_MODELS_DISCUSSIONS_FILE = DATA_DIRECTORY / 'quality_models_discussions.csv'
CLEANED_DISCUSSIONS_FILE = DATA_DIRECTORY / 'cleaned_discussions.csv'
# QUALITY_MODELS_QUESTIONS_FILE = QUALITY_FILTERED_DIRECTORY / 'quality_models_questions.csv'
#
# BERTOPIC_MODEL_ON_RAW = DATA_DIRECTORY / 'bertopic_model' / 'v1_raw_data' / 'model'
# BERTOPIC_MODEL_ON_BASIC = DATA_DIRECTORY / 'bertopic_model' / 'v3_basic_preprocessed_data' / 'model'
# BERTOPIC_MODEL_ON_SPEC = DATA_DIRECTORY / 'bertopic_model' / 'v2_specific_preprocessed_data' / 'model'
# BERTOPIC_MODEL_BEST_PRACTICE_ON_RAW = DATA_DIRECTORY / 'bertopic_model' / 'v4_best_practice_raw_data' / 'model'
# BERTOPIC_MODEL_BEST_PRACTICE_ON_CODE_REMOVED = DATA_DIRECTORY / 'bertopic_model' / 'v5_best_practice_code_removed_data' / 'model'
# BERTOPIC_MODEL_EXPERIMENT = DATA_DIRECTORY / 'bertopic_model' / 'v8_experiment_with_new_data' / 'model_min_cluster_size_60_topics_32'
# BERTOPIC_MODEL_UPDATED_LIBRARY = DATA_DIRECTORY / 'bertopic_model' / 'v9_updated_library' / 'model_min_cluster_size_60_topics_32'
#

BERTOPIC_MODEL_FILE = DATA_DIRECTORY / 'bertopic_model' / 'model_min_cluster_size_60'
#
# RANDOM_QUESTIONS_FILE = DATA_DIRECTORY / 'random_questions.csv'