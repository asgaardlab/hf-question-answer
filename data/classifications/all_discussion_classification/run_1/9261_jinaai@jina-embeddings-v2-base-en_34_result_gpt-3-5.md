## https://huggingface.co/jinaai/jina-embeddings-v2-base-en/discussions/34

contains_question: yes
question_part: If I try to run the example code
```python
from transformers import AutoModel

model = AutoModel.from_pretrained(
    "jinaai/jina-embeddings-v2-base-en", trust_remote_code=True
)  # trust_remote_code is needed to use the encode method
embeddings = model.encode(
    ["How is the weather today?", "What is the current weather like today?"]
)

print(embeddings.shape)
```

I get an output with shape `(2, 768)`, while on the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) the `embeddings dimension` is 512.