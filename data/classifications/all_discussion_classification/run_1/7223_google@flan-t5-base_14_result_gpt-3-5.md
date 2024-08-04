## https://huggingface.co/google/flan-t5-base/discussions/14

contains_question: yes

question_part: 
How come, no matter my learning rate, I end up having a prediction giving nans?
My inputs' max and min values are okay, the output's too, but for some reason I end up having nans.
I even instantly have nans if I train with a soft prompt self.trans(inputs_embeds=patch_emb) (min an max are okay).
When i predict, before training, the values are fine too. And if i train on bert and inject the information of the soft prompt by adding the same embedding on all the sequence it works fine.