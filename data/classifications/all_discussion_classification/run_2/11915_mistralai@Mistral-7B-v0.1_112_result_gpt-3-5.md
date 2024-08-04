## https://huggingface.co/mistralai/Mistral-7B-v0.1/discussions/112

contains_question: yes

question_part: My generation speed is so slow. It requires about 40-50s to generate one inference with max_new_token_length=128. It is much slower compared with mistral-8*7B. I wonder if I get wrong model files or my inference method is wrong. Also, it keeps notice me that `A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.` I am a bit confused about this part. I haven't set padding while training, is it a default value? Also, if my padding during training is right, why should I set it to left while generation?