## https://huggingface.co/HuggingFaceH4/starchat-alpha/discussions/6

contains_question: yes

question_part: What would cause this model to end up CPU bound while running inference? This is loaded to GPU but seems to be stuck doing some portion of the inference on CPU. I have the same issue whether loaded as AutoModelForCausalLM.from_pretrained and pipeline. Inference is *SUPER* slow and it won't load up my GPU much more then 30% on usage.