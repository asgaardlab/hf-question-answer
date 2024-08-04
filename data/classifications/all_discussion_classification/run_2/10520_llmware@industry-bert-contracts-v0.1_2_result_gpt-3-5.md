## https://huggingface.co/llmware/industry-bert-contracts-v0.1/discussions/2

contains_question: yes

question_part: - what kind of pooling method do we use to obtain embeddings from your models? I saw [here](https://github.com/llmware-ai/llmware/blob/main/llmware/models.py#L2123) that you use the CLS (i.e first embedding vector for HF) but would like to be sure
- do you normalize your embeddings ? 
- what kind of distance metric is to be used? L2 / dot ? 
- have you validated your models on some kind of industry retrieval benchmark ? if so would you be comfortable sharing it ?