## https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1/discussions/66

contains_question: yes

question_part: Mistral doesn't have a `pad_token_id`? 🤔

According to the [documentation](https://huggingface.co/docs/transformers/main/model_doc/mistral#transformers.MistralConfig.pad_token_id), the `pad_token_id` is optional?

I don't understand why, surely a padding token must have been used during training?