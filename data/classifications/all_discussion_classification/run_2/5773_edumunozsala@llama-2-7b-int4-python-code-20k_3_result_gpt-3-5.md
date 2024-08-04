## https://huggingface.co/edumunozsala/llama-2-7b-int4-python-code-20k/discussions/3

contains_question: yes
question_part: In the provided example you are using: model_id = "edumunozsala/llama-2-7b-int4-python-code-20k" but in the code you try to load it with "hf_model_repo": model = AutoModelForCausalLM.from_pretrained(hf_model_repo, load_in_4bit=True, torch_dtype=torch.float16, device_map=device_map) I believe you should use hf_model_id there.