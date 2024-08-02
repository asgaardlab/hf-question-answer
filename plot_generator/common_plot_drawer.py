import seaborn as sns
from matplotlib import pyplot as plt
from pandas import Series, DataFrame

from util import path


def draw_status_bar(data: Series, plot_title: str, save_file_name: str) -> None:
    value_counts = data.value_counts()
    print(plot_title)
    print(value_counts)
    plt.bar(value_counts.index, value_counts.values)
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.title(plot_title)
    save_file_name = save_file_name + '.png'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name)
    plt.show()


def draw_boxplot(data: Series, plot_title: str, x_label: str, save_file_name: str) -> None:
    print(plot_title)
    print(data.describe())
    print(f'median: {data.median()}')
    fig = plt.figure(figsize=(5, 1.25))
    with sns.axes_style('white'):
        fig.add_subplot()
        ax = sns.boxplot(data.values, orient='h', color='C0')
        sns.despine(ax=ax, top=True, right=True, left=False)

    plt.xscale('log')

    from matplotlib.ticker import LogFormatter
    formatter = LogFormatter(base=10, labelOnlyBase=False)
    plt.gca().xaxis.set_major_formatter(formatter)

    # plt.boxplot(data)
    plt.xlabel(x_label)
    plt.ylabel('')
    plt.yticks([])
    # plt.title(plot_title)
    fig.tight_layout()

    save_file_name_with_extension = save_file_name + '.png'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    save_file_name_with_extension = save_file_name + '.pdf'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    plt.show()


def draw_owner_response_bar(data: Series, plot_title: str, save_file_name: str) -> None:
    value_counts = data.value_counts()
    print(plot_title)
    print(value_counts)
    plt.bar(value_counts.index, value_counts.values, tick_label=['False', 'True'])
    plt.xlabel('Has owner response')
    plt.ylabel('Count')
    plt.title(plot_title)
    save_file_name = save_file_name + '.png'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name)
    plt.show()


def draw_discussion_comparison_multi_bar(data: DataFrame, plot_title: str, save_file_name: str) -> None:
    fig = plt.figure(figsize=(5, 2.5))

    with sns.axes_style('white'):
        ax = fig.add_subplot()
        ax = data.plot.barh(stacked=True, width=0.8, color=['C0', sns.xkcd_rgb['cool grey']], ax=ax)
        sns.move_legend(
            ax, "lower center",
            bbox_to_anchor=(.47, 1), ncol=2, title='', frameon=False,
        )
        sns.despine(ax=ax, top=True, left=False, bottom=False, right=True)
    #
    # total = 0
    # for patch in ax.patches:
    #     total += patch.get_width()
    #     if patch.get_width() == 0:
    #         continue
    #
    #     x, y = patch.get_xy()
    #     x += patch.get_width() - 1
    #     y += patch.get_height() / 2
    #     ax.annotate(str(int(patch.get_width())), (x, y), ha='right', va='center', color='white')
    #
    # for index in range(0, len(ax.containers[1].patches)):
    #     bar_total = 0
    #     for container in ax.containers:
    #         bar_total += container.patches[index].get_width()
    #     total_percentage = round((bar_total * 100.0) / total)
    #
    #     if total_percentage >= 13:
    #         patch = ax.containers[1].patches[index]
    #         x, y = patch.get_xy()
    #         x += patch.get_width() + 1
    #         y += patch.get_height() / 2
    #         ax.annotate(str(total_percentage) + '%', (x, y), ha='left', va='center', color='black')
    #
    plt.xlabel('Percentage of discussions')
    plt.ylabel('Discussion status')
    # plt.legend(title=legend_title)
    # plt.title(plot_title)

    plt.tight_layout()

    save_file_name_with_extension = save_file_name + '.png'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    save_file_name_with_extension = save_file_name + '.pdf'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    plt.show()


def draw_comparison_boxplot(data: DataFrame, x_label: str, y_label: str, plot_title: str, save_file_name: str) -> None:
    fig = plt.figure(figsize=(5.5, 2))
    with sns.axes_style('white'):
        fig.add_subplot()
        ax = sns.boxplot(data, x='data', y='label', orient='h', color='C0')
        sns.despine(ax=ax, top=True, right=True, left=False)

    plt.xscale('log')

    from matplotlib.ticker import LogFormatter
    formatter = LogFormatter(base=10, labelOnlyBase=False)
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    # plt.title(plot_title)
    fig.tight_layout()

    save_file_name_with_extension = save_file_name + '.png'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    save_file_name_with_extension = save_file_name + '.pdf'
    plt.savefig(path.GRAPH_DIRECTORY / save_file_name_with_extension)

    plt.show()
