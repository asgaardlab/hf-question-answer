import pandas as pd

from util import path


def models_statistics():
    all_models = pd.read_csv(path.ALL_MODELS_FILE)
    print(f'Total models: {len(all_models)}')


def model_discussion_statistics():
    non_empty_models = [model_dir for model_dir in path.DISCUSSIONS_DIRECTORY.iterdir() if
                        model_dir.is_dir() and any(model_dir.iterdir())]
    all_talk_files = list(path.DISCUSSIONS_DIRECTORY.glob('*/*.yaml'))
    print(f'{len(non_empty_models)} models have {len(all_talk_files)} community talks')

    discussions = [file_path for file_path in all_talk_files if file_path.name.startswith('discussion_')]
    pull_requests = [file_path for file_path in all_talk_files if file_path.name.startswith('pull_request_')]
    errors = [file_path for file_path in all_talk_files if file_path.name.endswith('error.yaml')]

    print(f'{len(discussions)} discussions')
    print(f'{len(pull_requests)} pull requests')
    print(f'{len(errors)} errors in discussions and pull requests')

    models_having_discussions = [model_dir for model_dir in non_empty_models if any(model_dir.glob('discussion_*.yaml'))]
    models_having_pull_requests = [model_dir for model_dir in non_empty_models if any(model_dir.glob('pull_request_*.yaml'))]

    print(f'{len(models_having_discussions)} models have discussions')
    print(f'{len(models_having_pull_requests)} models have pull requests')

    saved_discussions = pd.read_csv(path.ALL_DISCUSSIONS_FILE)
    print(f'{len(saved_discussions)} discussions are saved')


if __name__ == '__main__':
    models_statistics()
    model_discussion_statistics()
