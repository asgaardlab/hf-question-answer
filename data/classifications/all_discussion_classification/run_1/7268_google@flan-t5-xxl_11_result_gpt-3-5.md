## https://huggingface.co/google/flan-t5-xxl/discussions/11

contains_question: yes
question_part: The config.json says that the activation function is 'gelu' and yet 'is_gated_act' is set to true. Shouldn't the activation function be 'gated-gelu' like the rest of T5v1.1-style models? Or if that's not the case, shouldn't 'is_gated_act' be set to false?