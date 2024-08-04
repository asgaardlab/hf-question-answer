### Documents:
- Failed to load model

Here what i have here:
"Traceback (most recent call last):
File “X:\oobabooga_2\text-generation-webui\server.py”, line 102, in load_model_wrapper
shared.model, shared.tokenizer = load_model(shared.model_name)
File “X:\oobabooga_2\text-generation-webui\modules\models.py”, line 158, in load_model
model = load_quantized(model_name)
File “X:\oobabooga_2\text-generation-webui\modules\GPTQ_loader.py”, line 147, in load_quantized
exit()
File “X:\oobabooga_2\installer_files\env\lib_sitebuiltins.py”, line 26, in call
raise SystemExit(code)
SystemExit: None"

How can i fix it?
- Failed to load the model mpt-7b-storywriter.ggmlv3.q5_1.bin

When I try to load this model in ooba with my 8GB VRAM card, I get the following:

Traceback (most recent call last): File “F:\Programme\oobabooga_windows\text-generation-webui\server.py”, line 67, in load_model_wrapper shared.model, shared.tokenizer = load_model(shared.model_name, loader) File “F:\Programme\oobabooga_windows\text-generation-webui\modules\models.py”, line 74, in load_model output = load_func_maploader File “F:\Programme\oobabooga_windows\text-generation-webui\modules\models.py”, line 255, in llamacpp_loader model, tokenizer = LlamaCppModel.from_pretrained(model_file) File “F:\Programme\oobabooga_windows\text-generation-webui\modules\llamacpp_model.py”, line 55, in from_pretrained result.model = Llama(**params) File “F:\Programme\oobabooga_windows\installer_files\env\lib\site-packages\llama_cpp\llama.py”, line 289, in init assert self.ctx is not None AssertionError

Console says:
2023-07-03 08:38:29 INFO:Loading TheBloke_MPT-7B-Storywriter-GGML...
2023-07-03 08:38:29 INFO:llama.cpp weights detected: models\TheBloke_MPT-7B-Storywriter-GGML\mpt-7b-storywriter.ggmlv3.q5_1.bin

2023-07-03 08:38:29 INFO:Cache capacity is 0 bytes
llama.cpp: loading model from models\TheBloke_MPT-7B-Storywriter-GGML\mpt-7b-storywriter.ggmlv3.q5_1.bin
error loading model: llama.cpp: tensor 'rus' should not be 7-dimensional
llama_init_from_file: failed to load model
2023-07-03 08:38:30 ERROR:Failed to load the model.
Traceback (most recent call last):
  File "F:\Programme\oobabooga_windows\text-generation-webui\server.py", line 67, in load_model_wrapper
    shared.model, shared.tokenizer = load_model(shared.model_name, loader)
  File "F:\Programme\oobabooga_windows\text-generation-webui\modules\models.py", line 74, in load_model
    output = load_func_maploader
  File "F:\Programme\oobabooga_windows\text-generation-webui\modules\models.py", line 255, in llamacpp_loader
    model, tokenizer = LlamaCppModel.from_pretrained(model_file)
  File "F:\Programme\oobabooga_windows\text-generation-webui\modules\llamacpp_model.py", line 55, in from_pretrained
    result.model = Llama(**params)
  File "F:\Programme\oobabooga_windows\installer_files\env\lib\site-packages\llama_cpp\llama.py", line 289, in __init__
    assert self.ctx is not None
AssertionError

Exception ignored in: <function LlamaCppModel.__del__ at 0x00000270ED8DCA60>
Traceback (most recent call last):
  File "F:\Programme\oobabooga_windows\text-generation-webui\modules\llamacpp_model.py", line 29, in __del__
    self.model.__del__()
AttributeError: 'LlamaCppModel' object has no attribute 'model'

What are my chances, please?
- Error loading Q5_K_M with text-generation-webui

This model would not load, when using text-generation-webui. At least llama2_70b_chat_uncensored.Q5_K_M.gguf not loading.
What I get when press "load":
Traceback (most recent call last):

File “S:\oobabooga_windows\text-generation-webui\modules\ui_model_menu.py”, line 196, in load_model_wrapper

shared.model, shared.tokenizer = load_model(shared.model_name, loader)
File “S:\oobabooga_windows\text-generation-webui\modules\models.py”, line 79, in load_model

output = load_func_maploader
File “S:\oobabooga_windows\text-generation-webui\modules\models.py”, line 247, in llamacpp_loader

model, tokenizer = LlamaCppModel.from_pretrained(model_file)
File “S:\oobabooga_windows\text-generation-webui\modules\llamacpp_model.py”, line 105, in from_pretrained

result.model = Llama(**params)
File “S:\oobabooga_windows\installer_files\env\lib\site-packages\llama_cpp_ggml_cuda\llama.py”, line 328, in init

assert self.model is not None
AssertionError
### Keywords: webui, generation webui, text generation, generation, file, py, py line, text, line, oobabooga_windows