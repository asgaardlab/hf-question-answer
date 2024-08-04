## https://huggingface.co/elinas/alpaca-13b-lora-int4/discussions/8

contains_question: yes

question_part: After some trial and error I managed to load the tokenizer by setting use_fast=False. I'm trying to load the model using AutoModelForCausalLM.from_pretrained("elinas/alpaca-13b-lora-int4"), but I get errors on missing weight files. Am I missing something? I tried to load by setting use_safetensors=True, but I still get an error to ensure that the model has been saved with `safe_serialization=True`.