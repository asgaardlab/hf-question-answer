## https://huggingface.co/OpenLemur/lemur-70b-v1/discussions/2

contains_question: yes
question_part: Looks like the `max_position_embeddings` for Lemur-v1 Base was set to 2048: [link](https://huggingface.co/OpenLemur/lemur-70b-v1/blob/4946369eda79a5ddb5f53c0e2e387ada03a1feb3/config.json#L12). Is this intended? Or is this a typo since LLaMA supports 4096 from the beginning, and Lemur-v1-chat also has `max_position_embeddings` being 4096.