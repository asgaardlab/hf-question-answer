## https://huggingface.co/Deci/DeciLM-7B-instruct/discussions/8

contains_question: yes
question_part: how to save the model as a pytorch or tensorflow model, Is there a wat to save the model as a pytorch model instance instead of loading it every time with the transformers module? I have tried with wrapping the code inside a class that inherits `torch.nn.Module` but when I try to save the model (all the model not only the state dict) it throws an error.