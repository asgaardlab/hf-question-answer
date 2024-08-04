## https://huggingface.co/TheBloke/stable-vicuna-13B-GPTQ/discussions/18

contains_question: yes
question_part: Pardon me for asking this, but I have a very basic question about 4-bit quantization. How are these 4-bit quantized weights loaded in PyTorch (through HF `AutoModelForCausalLM` API) when PyTorch doesn't natively support `int4`?