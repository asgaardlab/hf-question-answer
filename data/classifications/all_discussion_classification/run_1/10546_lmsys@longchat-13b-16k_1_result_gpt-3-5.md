## https://huggingface.co/lmsys/longchat-13b-16k/discussions/1

contains_question: yes
question_part: I know that this model has it's own monkey patches for forward function and additional rotary positional embedding layer. But, because it's not added here, loading model blindly using transformers might not work as expected. At least put the monkey patches in the repo so user can load the model easily using transformers. Or you could add instruction to load the model in the model card.