import pandas as pd
from scipy.stats import mannwhitneyu

from data_analyzer.common_plot_drawer import draw_boxplot, draw_comparison_boxplot
from data_cleaner.discussion_reader import get_all_questions, get_quality_questions


def visualize_discussion_participants(discussions):
    if 'no_of_participants' not in discussions.columns:
        print('Error in data: Call calculate_discussions_participants()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    draw_boxplot(discussions['no_of_participants'], 'Distribution of number of participants per discussion', '# of participants per discussion', 'participants')


def compare_participants_by_status(discussions):
    if 'status' not in discussions.columns:
        print('Error in data: Call get_discussions_status()')
        return None

    if 'no_of_participants' not in discussions.columns:
        print('Error in data: Call calculate_discussions_participants()')
        return None

    open_discussions = discussions[discussions['status'] == 'open']['no_of_participants']
    print(f'Analysis of the number of participants per open discussion: \n{open_discussions.describe()}')
    print(f'median: {open_discussions.median()}')
    closed_discussions = discussions[discussions['status'] == 'closed']['no_of_participants']
    print(f'Analysis of the number of participants per closed discussion: \n{closed_discussions.describe()}')
    print(f'median: {closed_discussions.median()}')

    data = [
        ['Open', open_discussions],
        ['Closed', closed_discussions]
    ]
    data_df = pd.DataFrame(data, columns=['label', 'data'])
    data_df = data_df.explode('data')
    data_df['data'] = data_df['data'].astype('int')

    draw_comparison_boxplot(data_df, '# of participants per discussion', 'Discussion status',
                 'Comparison of number of participants per discussion status', 'participants_status')


def compare_response_by_team_participation(discussions):
    if 'has_owner_responses' not in discussions.columns:
        print('Error in data: Call calculate_has_owner_responses()')
        return None

    if 'no_of_contributor_responses' not in discussions.columns:
        print('Error in data: Call calculate_discussions_contributors_responses()')
        return None

    if 'no_of_responses' not in discussions.columns:
        print('Error in data: Call calculate_discussions_responses()')
        return None

    with_team_response = \
    discussions[(discussions['has_owner_responses'] == True) | (discussions['no_of_contributor_responses'] > 0)][
        'no_of_responses']
    print(f'Analysis of the number of responses per discussion having team response: \n{with_team_response.describe()}')
    print(f'median: {with_team_response.median()}')
    without_team_response = \
    discussions[(discussions['has_owner_responses'] == False) & (discussions['no_of_contributor_responses'] == 0)][
        'no_of_responses']
    print(
        f'Analysis of the number of responses per discussion having no team response: \n{without_team_response.describe()}')
    print(f'median: {without_team_response.median()}')

    data = [
        ['with participation', with_team_response],
        ['without participation', without_team_response]
    ]
    data_df = pd.DataFrame(data, columns=['label', 'data'])
    data_df = data_df.explode('data')
    data_df['data'] = data_df['data'].astype('int')

    draw_comparison_boxplot(data_df, '# of responses per discussion', '',
                            'Comparison of number of responses per discussion based on model team\'s participation',
                            'response_by_team_participation')


if __name__ == '__main__':
    # selected_discussions = get_selected_all_discussions()
    selected_discussions = get_quality_questions()

    visualize_discussion_participants(selected_discussions)
    compare_response_by_team_participation(selected_discussions)
    compare_participants_by_status(selected_discussions)
