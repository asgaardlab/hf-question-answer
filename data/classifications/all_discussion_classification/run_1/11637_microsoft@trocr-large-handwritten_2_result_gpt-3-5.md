## https://huggingface.co/microsoft/trocr-large-handwritten/discussions/2

contains_question: yes

question_part: After loading in the model, only about 3GB of memory is used up. However, the training step always returns the CUDA out of memory error. Steps to optimize the training have been carried out such as gradient checkpointing, mixed precision training and gradient accumulation. Are there any other optimizations that can  be carried out to make training possible, or 12GB is much too small to train the model.