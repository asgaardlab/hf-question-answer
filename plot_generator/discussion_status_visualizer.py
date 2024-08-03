import pandas as pd

from data_cleaner.discussion_reader import get_all_questions
from plot_generator.common_plot_drawer import draw_discussion_comparison_multi_bar, draw_boxplot


def visualize_discussion_status_by_team_participation(discussions):
    if 'status' not in discussions.columns:
        print('Error in data: Call get_discussions_status()')
        return None

    if 'has_owner_responses' not in discussions.columns:
        print('Error in data: Call calculate_has_owner_responses()')
        return None

    if 'no_of_contributor_responses' not in discussions.columns:
        print('Error in data: Call calculate_discussions_contributors_responses()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    # draw_status_bar(all_discussions['status'], 'Distribution of discussion status', 'status')

    all_discussions = discussions['status'].value_counts()
    print(f'All discussions: {all_discussions}')

    with_team_participation = discussions[(discussions['has_owner_responses'] == True) | (discussions['no_of_contributor_responses'] > 0)][
        'status'].value_counts()
    print(f'With team participation: {with_team_participation}')

    data = {
        'Category': ['Closed', 'Open'],
        'all_discussions': [all_discussions['closed'], all_discussions['open']],
        'with participation': [with_team_participation['closed'], with_team_participation['open']]
    }
    data_df = pd.DataFrame(data)
    data_df['without participation'] = data_df['all_discussions'] - data_df['with participation']
    data_df.drop('all_discussions', axis=1, inplace=True)
    print(data_df)
    data_percentage = data_df.set_index('Category').apply(lambda x: x / x.sum() * 100, axis=1)
    print(data_percentage)
    draw_discussion_comparison_multi_bar(data_percentage, 'Distribution of discussion status based on team participation',
                                         'status_by_team_participation')


def visualize_discussion_status_changes_count(discussions):
    if 'status_change_count' not in discussions.columns:
        print('Error in data: Call get_discussions_status_change_count()')
        return None

    print(f'Number of discussions: {len(discussions)}')
    print(f'More than 1 status change: {len(discussions[discussions["status_change_count"] > 1])}')
    draw_boxplot(discussions['status_change_count'], 'Distribution of status change count per discussion',
                 '# of status changes per discussion', 'status_change_count')


if __name__ == '__main__':
    # selected_discussions = get_selected_all_discussions()
    selected_discussions = get_all_questions()

    visualize_discussion_status_by_team_participation(selected_discussions)
    visualize_discussion_status_changes_count(selected_discussions)
