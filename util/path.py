from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


DATA_DIRECTORY = get_project_root() / 'data'
ALL_MODELS_FILE = DATA_DIRECTORY / 'all_models.csv'

DISCUSSIONS_DIRECTORY = DATA_DIRECTORY / 'discussions'
# CACHE_DIRECTORY = DATA_DIRECTORY / 'cache'
# DISCUSSION_FILE_PATHS_CACHE = CACHE_DIRECTORY / 'discussion_file_paths.pkl'
# DISCUSSIONS_CACHE = CACHE_DIRECTORY / 'discussions.pkl'
# PREPROCESSED_DISCUSSIONS_FILE = CACHE_DIRECTORY / 'preprocessed_discussions.csv'
# CLASSIFIED_DISCUSSIONS_FILE = DATA_DIRECTORY / 'classified_discussions.csv'
#
GRAPH_DIRECTORY = DATA_DIRECTORY / 'graphs'
# PRED_SCORE_PLOT_FILE = GRAPH_DIRECTORY / 'pred_score.png'
# BUG_PRED_SCORE_PLOT_FILE = GRAPH_DIRECTORY / 'bug_pred_score_plot.png'
# FEATURE_PRED_SCORE_PLOT_FILE = GRAPH_DIRECTORY / 'feature_pred_score_plot.png'
# QUESTION_PRED_SCORE_PLOT_FILE = GRAPH_DIRECTORY / 'question_pred_score_plot.png'
# DOCUMENTATION_PRED_SCORE_PLOT_FILE = GRAPH_DIRECTORY / 'documentation_pred_score_plot.png'
#
# PROMPTS_AND_RESULTS_DIRECTORY = DATA_DIRECTORY / 'prompts_and_results'
# UPDATED_PROMPT_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '3. updated_prompt'
# CLASSIFICATION_WITH_DESCRIPTION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '4. classification_with_class_description'
# BINARY_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '5. binary_classification'
# QUESTION_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '6. question_classification' / 'run_10'
#
# ALL_QUESTION_CLASSIFICATION_DIRECTORY = DATA_DIRECTORY / 'classifications' / '7. all_question_classification' / 'tie_breakers'
#
# CLASSIFICATION_DIRECTORY = ALL_QUESTION_CLASSIFICATION_DIRECTORY
#
# SYSTEM_PROMPT_FILE = CLASSIFICATION_DIRECTORY / '0_system_prompt.md'
# USER_PROMPT_FILE = CLASSIFICATION_DIRECTORY / '0_user_prompt.md'
#
# PROMPT_FILE = CLASSIFICATION_DIRECTORY / 'prompt.md'
#
ALL_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_discussions.csv'
ALL_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'all_random_discussions.csv'
#
# DISCUSSION_POSTS_FILE = CACHE_DIRECTORY / 'discussion_posts.pkl'
# RANDOM_DISCUSSION_POSTS_FILE = CACHE_DIRECTORY / 'random_discussion_posts.pkl'
# ALL_QUESTION_POSTS_FILE = CACHE_DIRECTORY / 'all_question_posts.pkl'
# QUALITY_QUESTION_POSTS_FILE = CACHE_DIRECTORY / 'quality_question_posts.pkl'
#
# SELECTED_RANDOM_DISCUSSIONS_FILE = DATA_DIRECTORY / 'selected_random_discussions.csv'
# SELECTED_ALL_DISCUSSIONS_FILE = DATA_DIRECTORY / 'selected_all_discussions.csv'
# ALL_QUESTIONS_FILE = DATA_DIRECTORY / 'all_questions.csv'
#
# TOPICS_DIRECTORY = DATA_DIRECTORY / 'topics' / 'train_v10'
#
# PREPROCESSED_POSTS_CACHE = CACHE_DIRECTORY / 'preprocessed_posts.pkl'
#
# QUALITY_FILTERED_DIRECTORY = DATA_DIRECTORY / 'quality_filtered'
QUALITY_MODELS_FILE = DATA_DIRECTORY / 'quality_models.csv'
QUALITY_MODELS_DISCUSSIONS_FILE = DATA_DIRECTORY / 'quality_models_discussions.csv'
CLEANED_QUALITY_MODELS_DISCUSSIONS_FILE = DATA_DIRECTORY / 'cleaned_quality_models_discussions.csv'
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
# BERTOPIC_MODEL = BERTOPIC_MODEL_UPDATED_LIBRARY
#
# RANDOM_QUESTIONS_FILE = DATA_DIRECTORY / 'random_questions.csv'