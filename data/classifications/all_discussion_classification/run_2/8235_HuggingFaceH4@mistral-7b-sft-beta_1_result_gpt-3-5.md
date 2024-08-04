## https://huggingface.co/HuggingFaceH4/mistral-7b-sft-beta/discussions/1

contains_question: yes

question_part: It appears that the weights of k_proj and v_proj have been altered, which contradicts the printed results. I'm curious to know if you manually adjusted the weights using the safe tensor file. Is there a bug present? Additionally, why are there two safe tensor files, resulting in a 7B model imposing a 14B memory burden