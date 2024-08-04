## https://huggingface.co/google/deplot/discussions/7

contains_question: yes
question_part: Hi,
I am trying to fine-tune the model by extending the vocabulary. To do this, I have added tokens and resized the embedding shape, but I would like to know how to directly access the weights since I will be initializing the newly added weights using different initialization options (random, Xavier, He, etc...). For the other transformer models, so is there a way to directly access the weights