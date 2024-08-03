from pathlib import Path

from bertopic import BERTopic

from discussion_topic_modeller.bertopic_topic_modeller import preprocess_data
from util import path


def get_topic_keywords(topic_id:int, topic_model: BERTopic) -> list[str]:
    topics = topic_model.get_topic_info()
    topic = topics[topics['Topic'] == topic_id]
    return topic['Representation'].values[0]


def get_topic_documents(topic_id: int, model: BERTopic) -> tuple[list[str], list[str]]:
    posts, urls = preprocess_data()
    documents = model.get_document_info(posts)

    topic_documents = documents[documents['Topic'] == topic_id]['Document'].values.tolist()
    return model.representative_docs_[topic_id], topic_documents


def list_documents_of_topic(topic_id: int, topic_model: BERTopic):
    representative_documents, all_topic_documents = get_topic_documents(topic_id, topic_model)
    print(f'-----------------------------Topic {topic_id} representative({len(representative_documents)}) documents:')
    for index, document in enumerate(representative_documents):
        print(f'========{index + 1}=========\n{document}')

    print(f'-----------------------------Topic {topic_id} all({len(all_topic_documents)}) documents:')
    for index, document in enumerate(all_topic_documents):
        print(f'========{index + 1}=========\n{document}')


def find_similar_questions(model_path: Path, question: str):
    topic_model = BERTopic.load(str(model_path.resolve()))
    similar_topics, similarity = topic_model.find_topics(question, top_n=1)

    print(similar_topics, similarity)

    list_documents_of_topic(similar_topics[0], topic_model)


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


def save_cluster_documents_and_keywords(model_path: Path, clustered_topic_ids: list[set[int]], file_name_prefix: str):
    model = BERTopic.load(str(model_path.resolve()))
    for index, topic_ids in enumerate(clustered_topic_ids):
        print(f'Cluster {index + 1}: {topic_ids}')
        cluster_documents = []
        cluster_keywords = []
        for topic_id in topic_ids:
            cluster_documents.extend(model.representative_docs_[topic_id])
            cluster_keywords.extend(get_topic_keywords(topic_id, model))

        clusters_directory = path.BERTOPIC_MODEL_FILE.parent / 'clusters'
        clusters_directory.mkdir(parents=True, exist_ok=True)

        string_topic_ids = map(str, topic_ids)
        file_name = f'{file_name_prefix}cluster_{"_".join(string_topic_ids)}.txt'

        with open(clusters_directory / file_name, 'w', encoding='utf-8') as file:
            file.write('### Documents:\n')
            for document in cluster_documents:
                file.write(f'- {document}\n')

            file.write('### Keywords: ')
            file.write(', '.join(cluster_keywords))


def save_topic_documents_and_keywords(model_path: Path, highest_topic_id: int, filename_prefix: str):
    model = BERTopic.load(str(model_path.resolve()))

    topics_directory = path.BERTOPIC_MODEL_FILE.parent / 'topics'
    topics_directory.mkdir(parents=True, exist_ok=True)

    for topic_id in range(highest_topic_id + 1):
        print(f'Topic {topic_id}')
        topic_documents = (model.representative_docs_[topic_id])
        topic_keywords = get_topic_keywords(topic_id, model)

        file_name = f'{filename_prefix}topic_{topic_id}.txt'

        with open(topics_directory / file_name, 'w', encoding='utf-8') as file:
            file.write('### Documents:\n')
            for document in topic_documents:
                file.write(f'- {document}\n')

            file.write('### Keywords: ')
            file.write(', '.join(topic_keywords))


if __name__ == '__main__':
    # save_cluster_documents_and_keywords(path.BERTOPIC_MODEL.parent / 'outlier_model_min_cluster_size_60_topics_4', [{0, 1, 2}], 'outlier_')
    save_topic_documents_and_keywords(path.BERTOPIC_MODEL_FILE, 2, 'model_')