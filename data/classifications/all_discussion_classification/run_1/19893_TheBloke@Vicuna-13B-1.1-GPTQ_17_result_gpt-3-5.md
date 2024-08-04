## https://huggingface.co/TheBloke/Vicuna-13B-1.1-GPTQ/discussions/17

contains_question: yes

question_part: When I do model.generate on a single sample it works fine. However, getting it to work on multiple samples of different length has been a challenge because there is no pad token in this model and my attempts to modify the embedding layer to include one (e.g. model.resize_token_embeddings(len(tokenizer)) have failed ('LlamaGPTQForCausalLM' object has no attribute 'resize_token_embeddings'). Has anyone gotten batch inference to work with this model, and if so how?