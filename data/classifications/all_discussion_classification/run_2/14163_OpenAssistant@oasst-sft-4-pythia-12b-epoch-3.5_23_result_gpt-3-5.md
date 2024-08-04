## https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5/discussions/23

contains_question: yes  
question_part: How to load this model in 4bit? I tried using BitsAndBytesConfig but seems not working, Loading in 16bit only when trying to load in 4bit  bnb_config = BitsAndBytesConfig(     load_in_4bit=True,     bnb_4bit_use_double_quant=True,     bnb_4bit_quant_type="nf4",     bnb_4bit_compute_dtype=torch.int8, )  model = AutoModelForCausalLM.from_pretrained("OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", quantization_config=bnb_config, device_map="auto")