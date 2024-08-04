## https://huggingface.co/mlx-community/Mistral-7B-Instruct-v0.2-4-bit/discussions/3

contains_question: yes

question_part: The quantized model config has rope_theta param, which was throwing an error as it was not used in model args. Removing this parameter worked for generation. @reach-vb how did you quantised the model