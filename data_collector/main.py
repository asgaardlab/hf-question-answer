from data_collector.statistics_provider import models_statistics, model_discussion_statistics
from model_discussion_collector import collect_discussions_of_models
from models_lister import get_all_models

if __name__ == '__main__':
    get_all_models()
    models_statistics()

    collect_discussions_of_models()
    model_discussion_statistics()
