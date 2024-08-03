from data_cleaner.discussion_reader import get_selected_all_discussions, get_cleaned_random_discussions


def provide_randon_discussion_classification_statistics():
    selected_random_discussions = get_cleaned_random_discussions()
    print(f'Cleaned random discussions: {len(selected_random_discussions)}')

    random_questions = selected_random_discussions[selected_random_discussions['contains_question_final_class'] == 'yes']
    print(f'Random questions: {len(random_questions)}')


def provide_all_discussion_classification_statistics():
    quality_discussions = get_selected_all_discussions()
    print(f'Cleaned discussions: {len(quality_discussions)}')

    questions = quality_discussions[quality_discussions['contains_question_final_class'] == 'yes']
    print(f'Questions: {len(questions)}')

    tie_breakers = quality_discussions[quality_discussions['contains_question_tie_breaker'] != 'error']
    print(f'Tie breakers: {len(tie_breakers)}')

    errors = quality_discussions[quality_discussions['contains_question_final_class'] == 'error']
    print(f'Errors: {len(errors)}')


if __name__ == '__main__':
    provide_randon_discussion_classification_statistics()
    provide_all_discussion_classification_statistics()
