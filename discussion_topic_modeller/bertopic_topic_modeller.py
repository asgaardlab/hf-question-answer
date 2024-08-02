import pickle
from pathlib import Path

import openai
from bertopic import BERTopic
from bertopic.representation import KeyBERTInspired, PartOfSpeech, MaximalMarginalRelevance, OpenAI
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP

from data_cleaner.discussion_reader import get_quality_questions
from data_cleaner.md_processor import remove_codeblock, remove_images, remove_emojis, remove_urls_from_hyperlinks, \
    remove_urls
from data_collector.type.discussion import Discussion
from util import path, constants
from util.helper import save_data_in_filepath


def load_dataset() -> dict:
    if path.QUALITY_QUESTION_POSTS_FILE.exists():
        with path.QUALITY_QUESTION_POSTS_FILE.open('rb') as file:
            return pickle.load(file)

    questions = get_quality_questions()
    questions['post'] = questions['discussion_path'].apply(
        lambda discussion_path: Discussion.from_path_str(discussion_path).get_post())
    question_posts = questions['post'].values.tolist()
    question_urls = questions['discussion_url'].values.tolist()
    classification_data = {'posts': question_posts, 'urls': question_urls}
    save_data_in_filepath(classification_data, path.QUALITY_QUESTION_POSTS_FILE)
    return classification_data


def remove_elements_from_post(post: str) -> str:
    post = remove_codeblock(post)
    post = remove_images(post)
    post = remove_emojis(post)
    post = remove_urls_from_hyperlinks(post)
    post = remove_urls(post)
    return post.strip()


def preprocess_data() -> tuple[list[str], list[str]]:
    questions = load_dataset()
    question_posts = questions['posts']
    question_urls = questions['urls']

    processed_posts = [remove_elements_from_post(post) for post in question_posts]

    return processed_posts, question_urls


def get_embedding_model() -> SentenceTransformer:
    sentence_transformer = SentenceTransformer('all-MiniLM-L6-v2')
    return sentence_transformer


def get_dimension_reduction_model() -> UMAP:
    umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric='cosine', random_state=42)
    return umap_model


def get_clustering_model(min_cluster_size) -> HDBSCAN:
    hdbscan_model = HDBSCAN(min_cluster_size=min_cluster_size, metric='euclidean', cluster_selection_method='eom',
                            prediction_data=True)
    return hdbscan_model


def get_vectorizer_model():
    vectorizer_model = CountVectorizer(stop_words="english", min_df=2, ngram_range=(1, 2))
    return vectorizer_model


def get_representation_model():
    keybert_model = KeyBERTInspired()
    pos_model = PartOfSpeech("en_core_web_sm")
    mmr_model = MaximalMarginalRelevance(diversity=0.3)

    prompt = """
    I have a topic that contains the following documents:
    [DOCUMENTS]
    The topic is described by the following keywords: [KEYWORDS]

    Based on the information above, extract a short but highly descriptive topic label of at most 5 words. Make sure it is in the following format:
    topic: <topic label>
    """
    client = openai.OpenAI(api_key=constants.OPENAI_API_KEY)
    openai_model = OpenAI(client, model="gpt-3.5-turbo", exponential_backoff=True, chat=True, prompt=prompt)

    # All representation models
    representation_model = {
        "KeyBERT": keybert_model,
        "OpenAI": openai_model,  # Uncomment if you will use OpenAI
        "MMR": mmr_model,
        "POS": pos_model
    }

    return representation_model


def train_model(dataset, min_cluster_size: int):
    print(f'Training model with {len(dataset)} posts')

    embedding_model = get_embedding_model()
    dimension_reduction_model = get_dimension_reduction_model()
    clustering_model = get_clustering_model(min_cluster_size)
    tokenizer = get_vectorizer_model()
    representation_model = get_representation_model()

    topic_model = BERTopic(

        # Pipeline models
        embedding_model=embedding_model,
        umap_model=dimension_reduction_model,
        hdbscan_model=clustering_model,
        vectorizer_model=tokenizer,
        representation_model=representation_model,

        # Hyperparameters
        top_n_words=10,
        calculate_probabilities=True,
        verbose=True
    )

    embeddings = embedding_model.encode(dataset, show_progress_bar=True)
    topic_model.fit_transform(dataset, embeddings)

    return topic_model


def save_model(topic_model, model_path):
    topic_model.representation_model = None  # Remove the representation model to get rid of "TypeError: cannot pickle '_thread.RLock' object" error
    path.BERTOPIC_MODEL.parent.mkdir(parents=True, exist_ok=True)
    topic_model.save(str(model_path.resolve()))


def split_documents(posts: list[str], model_path: Path):
    topic_model = BERTopic.load(str(model_path.resolve()))
    documents = topic_model.get_document_info(posts)

    main_documents_documents = documents[documents['Topic'] != -1]['Document'].values.tolist()
    print(f'Main documents: {len(main_documents_documents)}')
    outlier_documents_documents = documents[documents['Topic'] == -1]['Document'].values.tolist()
    print(f'Outlier documents: {len(outlier_documents_documents)}')

    return main_documents_documents, outlier_documents_documents


if __name__ == '__main__':
    posts, urls = preprocess_data()

    model = train_model(posts, min_cluster_size=60)
    save_model(model, path.BERTOPIC_MODEL)
    print(f'Model saved in {path.BERTOPIC_MODEL}')
