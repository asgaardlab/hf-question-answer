from pathlib import Path
from pprint import pprint

import pandas as pd
from bertopic import BERTopic

from discussion_topic_modeller.bertopic_topic_modeller import preprocess_data
from util import path


def get_topic_clusters(model_path: Path) -> list[set[int]]:
    topic_model = BERTopic.load(str(model_path.resolve()))

    posts, urls = preprocess_data()
    print(f'Number of posts: {len(posts)}')
    hierarchical_topics = topic_model.hierarchical_topics(posts)

    all_clusters = hierarchical_topics[hierarchical_topics['Distance'] < 1]
    cluster_topic_set = [set(cluster_topics) for cluster_topics in all_clusters['Topics'].values.tolist()]

    clusters = []
    for cluster_topics in cluster_topic_set:
        is_subset = False
        for index, topic in enumerate(cluster_topic_set):
            if cluster_topics != topic and cluster_topics.issubset(topic):
                is_subset = True
                break
        if not is_subset:
            clusters.append(cluster_topics)

    return clusters


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


def set_topic_labels(model_path: Path):
    model = BERTopic.load(str(model_path.resolve()))

    df = pd.read_csv(path.CUSTOM_LABELS_FILE)
    label_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
    model.set_topic_labels(label_dict)

    fig = model.visualize_hierarchy(title='', custom_labels=True)
    fig.show()
    save_file_path = model_path.parent / 'custom_label_hierarchy_plot.pdf'
    print(f'Saving to {save_file_path}')
    fig.write_image(save_file_path, engine='kaleido')


if __name__ == '__main__':
    cluster_topic_ids = get_topic_clusters(path.BERTOPIC_MODEL_FILE)
    print(cluster_topic_ids)

    visualize_topic_clusters(path.BERTOPIC_MODEL_FILE)
    set_topic_labels(path.BERTOPIC_MODEL_FILE)
