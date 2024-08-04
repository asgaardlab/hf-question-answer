## https://huggingface.co/openchat/openchat_3.5/discussions/42

contains_question: yes
question_part: Which is the actual way to store the Adapter after PEFT finetuning, whether it is 1 - Take the least loss checkpoint folder from the ```output_dir``` or 2 - save the adapter using ```trainer.save_model()``` or 3 - this method ```trainer.model.save_pretrained("path")```