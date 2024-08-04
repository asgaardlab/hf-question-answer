## https://huggingface.co/wukevin/tcr-bert/discussions/2

contains_question: yes

question_part: I would like to know the training settings for the weights of the masked amino acid model.
Is it the same as the ones described on the paper, as follows?
• Batch size:  256
• Learning rate warmup (number of training steps to linearly “ramp up” learning rate to specified value): 0
• Training epochs: 50
• Learning rate: 5e-5
The paper mentions that the number of training epochs is 50, but if early stopping was used, I would like to know the stopping epoch.
Also, what was the number of trainable parameters of the model shown in the paper? The model published in Hugginface seems to be 57 million, but is this the same as the parm number of the model of which results are reported in the paper?