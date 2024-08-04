## https://huggingface.co/bigscience/bloom/discussions/34

contains_question: yes
question_part: I was wondering what's the most efficient way to load partial model (num_layers<70) for bloom. One naive way could be to specify the number of layers in config and then load state dict with strict=False, but this would go through all the keys of 70 layers. Can there be a more efficient solution?