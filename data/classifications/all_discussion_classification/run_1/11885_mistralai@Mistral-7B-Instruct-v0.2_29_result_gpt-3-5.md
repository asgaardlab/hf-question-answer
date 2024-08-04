## https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/discussions/29

contains_question: yes
question_part: that is because according to the tokenizer config [here](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/blob/main/tokenizer_config.json), the chat template does not support system messages. So I'm wondering how the model was trained for supporting system messages and how should we use it