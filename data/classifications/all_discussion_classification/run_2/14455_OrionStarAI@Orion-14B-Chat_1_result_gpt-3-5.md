## https://huggingface.co/OrionStarAI/Orion-14B-Chat/discussions/1

contains_question: yes

question_part: I was trying to test out the model (to run JA MT-Bench) and was not getting very good results. One issue may be that the chat formatting is wrong - it appears to be Vicuna like, but the model card does not specify what system prompts should look like. One thing that might help with formatting would be to add a `chat_template` to the `tokenizer_config.json`?