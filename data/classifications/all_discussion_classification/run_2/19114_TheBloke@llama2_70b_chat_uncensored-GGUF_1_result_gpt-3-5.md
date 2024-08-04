## https://huggingface.co/TheBloke/llama2_70b_chat_uncensored-GGUF/discussions/1

contains_question: yes

question_part: This model would not load, when using text-generation-webui. At least llama2_70b_chat_uncensored.Q5_K_M.gguf not loading. What I get when press "load": Traceback (most recent call last):

File “S:\oobabooga_windows\text-generation-webui\modules\ui_model_menu.py”, line 196, in load_model_wrapper

shared.model, shared.tokenizer = load_model(shared.model_name, loader)
File “S:\oobabooga_windows\text-generation-webui\modules\models.py”, line 79, in load_model

output = load_func_map[loader](model_name)
File “S:\oobabooga_windows\text-generation-webui\modules\models.py”, line 247, in llamacpp_loader

model, tokenizer = LlamaCppModel.from_pretrained(model_file)
File “S:\oobabooga_windows\text-generation-webui\modules\llamacpp_model.py”, line 105, in from_pretrained

result.model = Llama(**params)
File “S:\oobabooga_windows\installer_files\env\lib\site-packages\llama_cpp_ggml_cuda\llama.py”, line 328, in init

assert self.model is not None
AssertionError