## https://huggingface.co/forestai/fireact_llama_2_13b_lora/discussions/1

contains_question: yes

question_part: Above is my finetuning code. I am trying to finetune meta-llama/Llama-2-13b-chat-hf, but running into error: 
self.is_model_parallel = self.args.device != torch.device(devices[0])
IndexError: list index out of range

When I remove device_map="auto", there are other error line NotImplementedError: Cannot copy out of meta tensor; no data!

And when I set device_map completely on GPU, using {"":0}, I am getting error:RuntimeError: No CUDA GPUs are available

Is there any particular solution around it as I am new to all this. I am running this in gcp g2-standard-12 VM with nvidia L4 GPU. GPU memory is maybe around 24gb