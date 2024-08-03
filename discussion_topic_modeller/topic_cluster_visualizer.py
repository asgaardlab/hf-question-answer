from pathlib import Path

from bertopic import BERTopic

from util import path


def visualize_topic_clusters(model_path: Path):
    model = BERTopic.load(str(model_path.resolve()))

    chatgpt_topic_labels = {topic: " | ".join(list(zip(*values))[0]) for topic, values in
                            model.topic_aspects_["OpenAI"].items()}
    model.set_topic_labels(chatgpt_topic_labels)

    fig = model.visualize_hierarchy(title='', custom_labels=True)
    fig.show()
    save_file_path = model_path.parent / f'{model_path.name}_hierarchy_plot.pdf'
    print(f'Saving to {save_file_path}')
    fig.write_image(save_file_path, engine='kaleido')


if __name__ == '__main__':
    visualize_topic_clusters(path.BERTOPIC_MODEL_FILE)
