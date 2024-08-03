import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

from util import path


def visualize_model_likes_distribution(models):
    print(f'Model likes:\n{models["likes"].describe()}')
    models['likes'].plot.hist(bins=500, alpha=0.5)

    plt.yscale('log')

    plt.title('Model likes')
    plt.xlabel('Likes')
    plt.tight_layout()
    plt.savefig(path.PLOTS_DIRECTORY / 'model_likes_distribution.png')
    plt.show()

    filtered_models = models[models['likes'] > 24]
    print(f'Filtered model likes:\n{filtered_models["likes"].describe()}')


def visualize_model_downloads_distribution(models):
    print(f'Model downloads:\n{models["downloads"].describe()}')
    models['downloads'].plot.hist(bins=500, alpha=0.5)

    plt.yscale('log')

    def format_tick(x, pos):
        if x == 0:
            return '0'
        return f'{x / 1e6:.0f}M'
    plt.gca().xaxis.set_major_formatter(FuncFormatter(format_tick))

    plt.title('Model downloads')
    plt.xlabel('Downloads (M = million)')
    plt.tight_layout()
    plt.savefig(path.PLOTS_DIRECTORY / 'model_downloads_distribution.png')
    plt.show()

    filtered_models = models[models['downloads'] > 24]
    print(f'Filtered model downloads:\n{filtered_models["downloads"].describe()}')


if __name__ == '__main__':
    all_models = pd.read_csv(path.ALL_MODELS_FILE)

    visualize_model_likes_distribution(all_models)
    visualize_model_downloads_distribution(all_models)