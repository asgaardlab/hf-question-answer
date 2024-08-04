## https://huggingface.co/sentence-transformers/all-mpnet-base-v2/discussions/4

contains_question: yes

question_part: With a simple encoded_input of 512 tokens, the model takes around 230ms to compute the embedding, with the array shape (2, 512) taking 2000ms and increasing exponentially, is there any way I can achieve low latency using the model for long documents 