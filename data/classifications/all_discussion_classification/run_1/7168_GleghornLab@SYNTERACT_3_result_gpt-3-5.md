## https://huggingface.co/GleghornLab/SYNTERACT/discussions/3

contains_question: yes

question_part: Random train/test split? It mentions in the paper that you randomly selected sequences for the test dataset. Shouldn't we consider something like sequence similarity and also make sure there are no sequences in the test dataset that are also in the training dataset to prevent data leakage? I was thinking perhaps clustering protein-protein complexes using a protein language model might be helpful in this regard. Also, do you have code released for how you trained the model? I would like to try to replicate what you have done and perhaps also use a different train/test split.