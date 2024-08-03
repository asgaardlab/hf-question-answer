from pathlib import Path

from pandas import DataFrame

from data_cleaner.discussion_reader import get_cleaned_all_discussions, save_cleaned_all_discussions


def read_class_from_result_file(result_file_path: Path) -> str:
    with open(result_file_path, 'r', encoding='utf-8') as f:
        result = f.read()
        gpt_output = result.split('\n\n')[1]
        result_line = gpt_output.strip().splitlines()[0].strip()
        contains_question = result_line.split(':')[1].strip().lower()

        return contains_question


def get_gpt_classes(discussions, result_directory, class_column_name: str) -> DataFrame:
    result_files = result_directory.glob('*_result_gpt-3-5.md')

    contains_questions = {}
    for result_file in result_files:
        discussion_index = int(result_file.name.split('_')[0])
        contains_question = read_class_from_result_file(result_directory / result_file)

        print(f'{discussion_index}\ncontains_question: {contains_question}')
        if not contains_question in ['yes', 'no']:
            contains_questions[discussion_index] = 'error'
        else:
            contains_questions[discussion_index] = contains_question

    discussions[class_column_name] = discussions['index'].map(contains_questions)
    return discussions


def get_final_class(discussion: DataFrame, tie_breaking_column_name: str) -> str:
    if discussion['contains_question_run_1'] == 'error' or discussion['contains_question_run_2'] == 'error':
        return 'error'
    elif discussion['contains_question_run_1'] == discussion['contains_question_run_2']:
        return discussion['contains_question_run_1']
    else:
        return discussion[tie_breaking_column_name]


def get_all_questions() -> DataFrame:
    selected_all_discussions = get_cleaned_all_discussions()
    return selected_all_discussions[selected_all_discussions['contains_question_final_class'] == 'yes']
