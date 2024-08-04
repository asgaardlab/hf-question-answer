## https://huggingface.co/tiiuae/falcon-7b/discussions/27

contains_question: yes

question_part: For some reason, the class "Attention" module produces a shape mismatch error when it goes to this branch as below. It complains that self.num_heads is not equal to self.num_kv, which will happen because the model config default value for num_kv is 1.