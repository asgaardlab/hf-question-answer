## https://huggingface.co/tiiuae/falcon-40b/discussions/60

contains_question: yes  
question_part: Keep getting the following error even after usingtokenizer = AutoTokenizer.from_pretrained("/falcon-40b",return_token_type_ids=False)model = AutoModelForCausalLM.from_pretrained("/falcon-40b", trust_remote_code=True, torch_dtype="auto", device_map="auto)tokens = model.generate(**input_ids)ValueError: The following `model_kwargs` are not used by the model: ['token_type_ids'] (note: typos in the generate arguments will also show up in this list)