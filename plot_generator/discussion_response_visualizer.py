import pandas as pd
from scipy.stats import mannwhitneyu

from data_analyzer.common_plot_drawer import draw_boxplot, draw_owner_response_bar, \
    draw_comparison_boxplot
from data_cleaner.discussion_reader import get_quality_questions


def visualize_discussion_response(discussions):
    if 'no_of_responses' not in discussions.columns:
        print('Error in data: Call calculate_discussions_responses()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    print(f'Discussions with response: {len(discussions[discussions["no_of_responses"] > 0])}')
    draw_boxplot(discussions['no_of_responses'], 'Distribution of number of responses per discussion',
                 '# of responses per discussion', 'response')


def visualize_owner_response_discussion(discussions):
    if 'has_owner_responses' not in discussions.columns:
        print('Error in data: Call calculate_has_owner_responses()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    draw_owner_response_bar(discussions['has_owner_responses'], 'Distribution of owner response', 'owner_response')


def compare_response_by_status(discussions):
    if 'status' not in discussions.columns:
        print('Error in data: Call get_discussions_status()')
        return None

    if 'no_of_responses' not in discussions.columns:
        print('Error in data: Call calculate_discussions_responses()')
        return None

    open_no_of_responses = discussions[discussions['status'] == 'open']['no_of_responses']
    print(f'Analysis of the number of responses per open discussion: \n{open_no_of_responses.describe()}')
    print(f'median: {open_no_of_responses.median()}')
    print(f'{len(open_no_of_responses[open_no_of_responses == 0])} discussions are open without any responses')
    closed_no_of_responses = discussions[discussions['status'] == 'closed']['no_of_responses']
    print(f'Analysis of the number of responses per closed discussion: \n{closed_no_of_responses.describe()}')
    print(f'median: {closed_no_of_responses.median()}')
    print(
        f'{len(closed_no_of_responses[closed_no_of_responses == 0])} discussions have been closed without any responses')
    data = [
        ['Open', open_no_of_responses],
        ['Closed', closed_no_of_responses]
    ]
    data_df = pd.DataFrame(data, columns=['label', 'data'])
    data_df = data_df.explode('data')
    data_df['data'] = data_df['data'].astype('int')

    draw_comparison_boxplot(data_df, '# of responses per discussion', 'Discussion status',
                            'Comparison of number of responses per discussion status', 'response_by_status')


def visualize_response_length(discussions):
    if 'responses_length_per_word_count' not in discussions.columns:
        print('Error in data: Call calculate_response_length()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    draw_boxplot(discussions['responses_length_per_word_count'], 'Distribution of response length per word count',
                 'Response length (word count)', 'response_length')


def compare_response_length_per_status(discussions):
    if 'status' not in discussions.columns:
        print('Error in data: Call get_discussions_status()')
        return None

    if 'responses_length_per_word_count' not in discussions.columns:
        print('Error in data: Call calculate_response_length()')
        return None

    open_responses_length = discussions[discussions['status'] == 'open']['responses_length_per_word_count']
    print(f'Analysis of the response length per word count for open discussions: \n{open_responses_length.describe()}')
    print(f'median: {open_responses_length.median()}')

    closed_responses_length = discussions[discussions['status'] == 'closed']['responses_length_per_word_count']
    print(f'Analysis of the response length per word count for closed discussions: \n{closed_responses_length.describe()}')
    print(f'median: {closed_responses_length.median()}')

    data = [
        ['Open', open_responses_length],
        ['Closed', closed_responses_length]
    ]
    data_df = pd.DataFrame(data, columns=['label', 'data'])
    data_df = data_df.explode('data')
    data_df['data'] = data_df['data'].astype('int')

    draw_comparison_boxplot(data_df, 'Response length (word count)', 'Discussion status',  'Comparison of response length based on discussion status', 'response_length_by_status')


if __name__ == '__main__':
    # selected_discussions = get_selected_all_discussions()
    selected_discussions = get_quality_questions()

    visualize_discussion_response(selected_discussions)
    visualize_owner_response_discussion(selected_discussions)

    compare_response_by_status(selected_discussions)

    visualize_response_length(selected_discussions)
    compare_response_length_per_status(selected_discussions)
