## https://huggingface.co/mosaicml/mpt-7b/discussions/10

contains_question: yes
question_part: Hi, I'm trying to train this model using LoRA, but I'm unable to find the query_key_value for this model. For LLaMA, it was v_proj and q_proj, but I'm not sure about this one. I'm using the finetune.py script from https://github.com/leehanchung/mpt-lora where there is "query_key_value" and "xxx" but that also yields the "ValueError: Target modules ['query_key_value', 'xxx'] not found in the base model. Please check the target modules and try again." error.

If anyone knows what they are or how to find them, please let me know.