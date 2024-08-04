## https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/discussions/57

contains_question: yes

question_part: Can you please clarify how you use the `max_position_embeddings` hyperparameter. The `config.json` file [specifies](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/blob/7ad5799710574ba1c1d953eba3077af582f3a773/config.json#L11) `max_position_embeddings=32768` while the paper claims an attention span of 131K tokens (see [Section 2 on "Architectural details" → "Sliding Window Attention"](https://arxiv.org/pdf/2310.06825.pdf)).