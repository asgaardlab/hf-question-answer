## https://huggingface.co/TheBloke/Wizard-Vicuna-30B-Uncensored-GPTQ/discussions/15

contains_question: yes

question_part: Hi, I can load this model using Oobabooga autogptq, but get the error in the title in a notebook. I'm using a rtx 4090 with 64gb of ram. Below is my command to load:

model = AutoGPTQForCausalLM.from_quantized(pretrained_model_dir, use_safetensors=True,\
        model_basename=model_basename,low_cpu_mem_usage=True,device_map="auto", use_triton=False)

Any clue what the problem may be?