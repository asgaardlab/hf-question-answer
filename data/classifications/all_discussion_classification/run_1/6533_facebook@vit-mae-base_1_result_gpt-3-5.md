## https://huggingface.co/facebook/vit-mae-base/discussions/1

contains_question: yes  
question_part: Why the sequence length is not the equal to the number of patches? The `last_hidden_state` of the model outputs arrays of shape `(batch_size, sequence_length, hidden_dim)`. The `sequence_length` is 50 but from my understanding of the ViT paper it should be equal to the number of patches `224*224 / 16*16 = 196`. I checked the [original model](https://github.com/facebookresearch/mae) and there the `sequence_length` is indeed 196. What am I missing?