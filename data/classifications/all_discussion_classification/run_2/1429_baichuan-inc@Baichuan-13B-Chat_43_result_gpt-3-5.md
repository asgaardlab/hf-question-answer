## https://huggingface.co/baichuan-inc/Baichuan-13B-Chat/discussions/43

contains_question: yes

question_part: Hi, when I use AutoModelForCausalLM.from_config to get Baichuan model, I have found that even though the GenerationConfig.from_model_config function is called here(https://github.com/huggingface/transformers/blob/ef10dbce5cbc9a8b6a0a90b04378ca96f4023aa1/src/transformers/generation/utils.py#L1415), repetition_penalty is not set. So, when we use from_config API, we can't get right accuracy. Please check from_config api for Baichuan.