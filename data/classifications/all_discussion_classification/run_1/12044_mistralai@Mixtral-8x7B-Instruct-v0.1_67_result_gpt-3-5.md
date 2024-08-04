## https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1/discussions/67

contains_question: yes

question_part: Which is the actual way to store the adapters after PEFT finetuning, So I bit confused. Which is the actual way to store the adapter after PEFT based lora fine-tuning whether it is 1 - Take the least loss checkpoint folder from the ```output_dir``` or 2 - save the adapter using ``` trainer.save_model() ``` or 3 - this method ``` trainer.model.save_pretrained("path") ```