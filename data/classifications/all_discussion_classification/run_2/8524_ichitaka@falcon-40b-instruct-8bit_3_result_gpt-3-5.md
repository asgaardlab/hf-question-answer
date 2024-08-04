## https://huggingface.co/ichitaka/falcon-40b-instruct-8bit/discussions/3

contains_question: yes

question_part: How did you manage to quantize the model? I was also trying to quantize some 40B/30B LLM models using bitsandbytes and AUTOGPTQ algorithm, with bits and bytes it was giving me errors, with layers, it would be extremely helpful if you can give insight into how did you manage to quantize this model? Also `model.save_pretrained()` after `load_in_8bit=True` gives an error that a quantized model cannot be saved. How did you push it here?