import pandas as pd
import pytz
import seaborn as sns
from matplotlib import pyplot as plt

from data_analyzer.common_plot_drawer import draw_boxplot
from data_cleaner.discussion_reader import get_all_discussions, get_all_questions, get_quality_questions
from util import path


def visualize_discussion_creation_time_range(discussions):
    print(len(discussions))
    discussion_creation_dates = discussions['discussion_created_at']
    discussion_creation_dates.index = pd.to_datetime(discussion_creation_dates, utc=True)

    print(discussion_creation_dates.min(), discussion_creation_dates.max())

    monthly_counts = discussion_creation_dates.resample('M').size()
    print(monthly_counts)
    print(monthly_counts.mean())

    sns.set_style('whitegrid')
    monthly_counts.plot(kind='bar')

    new_xtick_labels = []
    for index in monthly_counts.index:
        # print(f'{index}: {monthly_counts[index]}')
        new_xtick_labels.append(index.strftime('%b %Y'))

    plt.gca().set_xticklabels(new_xtick_labels)

    # plt.xticks(rotation=45)

    # plt.title('Discussion creation time range')
    plt.xlabel('Time (Month-Year)')
    plt.ylabel('# of new discussions posted on the month')
    plt.tight_layout()
    plt.savefig(path.GRAPH_DIRECTORY / 'discussions_increase_rate.pdf', dpi=300)
    plt.show()


def visualize_discussion_response_delays(discussions):
    print(f'Number of discussions: {len(discussions)}')

    open_discussions = discussions[discussions['status'] == 'open']
    open_discussions_without_response = open_discussions[open_discussions['no_of_responses'] == 0]
    print(f'Open discussions without response: {len(open_discussions_without_response)}')

    post_times = pd.to_datetime(open_discussions_without_response['discussion_created_at'])
    post_times_sorted =  post_times.sort_values(ascending=False)
    print(post_times_sorted.head(20))

    last_response = post_times.max()
    before_24_hrs = last_response - pd.Timedelta(days=1)
    print(last_response, before_24_hrs)
    post_times_before_24_hrs = post_times[post_times < before_24_hrs]
    print(f'Open for more than 24 hours: {len(post_times_before_24_hrs)}')

    discussions_with_response = discussions[discussions['no_of_responses'] > 0]
    print(f'Discussions with response: {len(discussions_with_response)}')

    response_delays = pd.to_timedelta(discussions_with_response['discussion_response_delay']).dt.days
    print(response_delays.describe())
    print(f'median: {response_delays.median()}')
    print(f'< 24 hours: {len(response_delays[response_delays < 1])}')

    open_discussions_with_responses = open_discussions[open_discussions['no_of_responses'] > 0]
    response_delays = pd.to_timedelta(open_discussions_with_responses['discussion_response_delay']).dt.days
    print(f'Open discussions with response:\n{response_delays.describe()}\nmedian: {response_delays.median()}')

    closed_discussions_with_responses = discussions_with_response[discussions_with_response['status'] == 'closed']
    response_delays = pd.to_timedelta(closed_discussions_with_responses['discussion_response_delay']).dt.days
    print(f'Closed discussions with response:\n{response_delays.describe()}\nmedian: {response_delays.median()}')

    draw_boxplot(response_delays, 'Distribution of response delay per discussion', 'Delay (in days)', 'response_delay')


if __name__ == '__main__':
    selected_discussions = get_all_discussions()
    visualize_discussion_creation_time_range(selected_discussions)

    selected_discussions = get_quality_questions()
    visualize_discussion_response_delays(selected_discussions)