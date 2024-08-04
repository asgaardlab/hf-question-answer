## https://huggingface.co/BelleGroup/BELLE-7B-2M/discussions/3

contains_question: yes

question_part: Hi team, I got an error when I try to use the model: ` Unable to load weights from pytorch checkpoint file` This is what I tried to do: ``` tokenizer = AutoTokenizer.from_pretrained("BelleGroup/BELLE-7B-2M") model = AutoModel.from_pretrained("BelleGroup/BELLE-7B-2M") ``` Any idea?