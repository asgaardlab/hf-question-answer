## https://huggingface.co/kaist-ai/prometheus-13b-v1.0/discussions/1

contains_question: yes
question_part: For 16f model, is it mandatory to use "tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf") model = LlamaForCausalLM.from_pretrained("kaist-ai/Prometheus-13b-v1.0", device_map="auto", torch_dtype=torch.float16)" or "tokenizer = AutoTokenizer.from_pretrained("kaist-ai/prometheus-13b-v1.0") model = AutoModelForCausalLM.from_pretrained("kaist-ai/prometheus-13b-v1.0", device_map="auto", torch_dtype=torch.float16)" will also work?