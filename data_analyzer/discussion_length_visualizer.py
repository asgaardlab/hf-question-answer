from matplotlib import pyplot as plt
from pandas import DataFrame

from data_cleaner.discussion_length_calculator import calculate_random_discussion_lengths, \
    calculate_all_discussion_lengths
from data_cleaner.discussion_reader import get_all_random_discussions, get_all_discussions
from util import path


def visualize_discussion_length_distribution(discussions: DataFrame, title: str) -> None:
    lengths = discussions['length']
    quartiles = lengths.quantile([0.25, 0.5, 0.75])

    print(f'===============Length statistics for {title} discussions')
    print(f'Range: {lengths.min()} - {lengths.max()}')
    print(f'Mean: {lengths.mean()}\nMedian: {lengths.median()}\nMode: {lengths.mode().tolist()}')
    print(f'Standard deviation: {lengths.std()}\nVariance: {lengths.var()}')
    print(
        f'Percentile [25th, 50th, 75th]: [{quartiles[0.25]}, {quartiles[0.5]}, {quartiles[0.75]}]')
    q1 = lengths.quantile(0.25)
    q3 = lengths.quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    print(f'Lower outliers: {lengths[lengths < lower_bound].tolist()}')
    print(f'Upper outliers: {lengths[lengths > upper_bound].sort_values().tolist()}')
    print(f'{len(lengths[lengths < lower_bound]) + len(lengths[lengths > upper_bound])} removed outliers')

    min_length = 50

    print(f'{len(lengths[lengths < min_length])} random discussions have length less than {min_length}')

    filtered_lengths = lengths[(lengths >= lower_bound) & (lengths <= upper_bound)]
    # filtered_lengths = lengths[lengths < 500]
    filtered_lengths.plot(kind='hist', bins=100, alpha=0.5)

    plt.title(f'{title} Discussion Length Distribution')
    plt.xlabel('Discussion Length')
    plt.ylabel('Frequency')

    plt.savefig(path.GRAPH_DIRECTORY / f'{title.lower()}_discussion_length_distribution.png')
    plt.show()


def visualize_random_discussion_length_distribution() -> None:
    random_discussions = get_all_random_discussions()
    if 'length' not in random_discussions.columns:
        random_discussions = calculate_random_discussion_lengths()

    visualize_discussion_length_distribution(random_discussions, 'Random')


def visualize_all_discussion_length_distribution() -> None:
    all_discussions = get_all_discussions()
    if 'length' not in all_discussions.columns:
        all_discussions = calculate_all_discussion_lengths()
    visualize_discussion_length_distribution(all_discussions, 'All')


if __name__ == '__main__':
    visualize_random_discussion_length_distribution()
    visualize_all_discussion_length_distribution()
