from typing import Iterable

import pandas as pd
from huggingface_hub import HfApi
from huggingface_hub.hf_api import ModelInfo

from util import path


def to_array(model: ModelInfo) -> list[str | None | dict]:
    library_name = model.library_name if hasattr(model, 'library_name') else None
    return [model.author, model.id, model.modelId, model.pipeline_tag, model.downloads, model.likes, model.lastModified,
            model.sha, library_name, model.private, model.tags]


def get_all_models() -> Iterable[ModelInfo]:
    print('Fetching model list...')
    api = HfApi()
    models = api.list_models(
        full=True,
        cardData=False,
        fetch_config=False
    )

    model_list = [to_array(model) for model in models]
    data_df = pd.DataFrame(model_list,
                           columns=['author', 'id', 'model_id', 'pipeline_tag', 'downloads', 'likes', 'last_modified',
                                    'sha', 'library_name', 'private', 'tags'])

    path.ALL_MODELS_FILE.parent.mkdir(parents=True, exist_ok=True)
    data_df.to_csv(path.ALL_MODELS_FILE, index=False)

    return models


if __name__ == '__main__':
    get_all_models()
