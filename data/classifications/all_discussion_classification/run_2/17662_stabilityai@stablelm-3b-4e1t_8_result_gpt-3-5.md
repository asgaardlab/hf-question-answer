## https://huggingface.co/stabilityai/stablelm-3b-4e1t/discussions/8

contains_question: yes

question_part: I want to further train this model to fit my data. I am trying to add data at the pretraining level, but it seems to take a long time because there is no flash attention in the modeling code. Can you please add a class Attention with flash attention in modeling_stablelm_epoch.py and add some code for supporting flash attention in stablelm model