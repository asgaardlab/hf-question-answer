## https://huggingface.co/IDEA-CCNL/Taiyi-Stable-Diffusion-1B-Chinese-v0.1/discussions/16

contains_question: yes

question_part: If padding mode is set to 'max_length', it will raise overflow. Actually, I think this is a typo once you print out `tokenizer.model_max_len`, which is quite abnormal.