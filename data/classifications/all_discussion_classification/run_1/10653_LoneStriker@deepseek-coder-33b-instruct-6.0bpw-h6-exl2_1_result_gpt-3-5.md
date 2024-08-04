## https://huggingface.co/LoneStriker/deepseek-coder-33b-instruct-6.0bpw-h6-exl2/discussions/1

contains_question: yes

question_part: The tokenizer_config.json specifies an eos_token of "< | end_of_sentence | >" but the config.json has an eos_token_id 32021 which is "<|EOT|>"; this means you get garbage post-generation to fill the whole max tokens if the software you are using reads the eos_token from the tokenizer config rather than the config.json.