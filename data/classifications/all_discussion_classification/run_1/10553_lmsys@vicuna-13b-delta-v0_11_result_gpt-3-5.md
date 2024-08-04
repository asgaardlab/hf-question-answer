## https://huggingface.co/lmsys/vicuna-13b-delta-v0/discussions/11

contains_question: yes

question_part: size mismatch for lm_head.weight: copying a param with shape torch.Size([32000, 5120]) from checkpoint, the shape in current model is torch.Size([32001, 5120]).
I use vicuna-1.5 to finetune a text2SQL model. And I downloaded the model files from https://huggingface.co/lmsys/vicuna-13b-v1.5.
But when I started to train the model, just found this error. Anyone can provide some help? It confused me a week.