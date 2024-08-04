## https://huggingface.co/ctheodoris/Geneformer/discussions/131

contains_question: yes

question_part: Hi, I want to create the token embeddings for the vocabulary. So that I can add the position embedding and token embedding as the input of my customised model. Currently I am using the following token_embed = nn.Embedding(target_vocab_size, d_model).to(device) but this token embeddings won't match to Geneformer's embedding. So can you please guide me what you have used to create the token embeddings for complete vocabulary.