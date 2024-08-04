## https://huggingface.co/uclanlp/scibart-base/discussions/2

contains_question: yes
question_part: Could you please provide more information on how to use the model and tokenizer? The config file has "tokenizer_class": "SciBartTokenizer" but SciBartTokenizer is not a Huggingface Tokenizer class. Therefore, when I use AutoTokenizer.from_pretrained("scibart-base") or BartTokenizer.from_pretrained("scibart-base"), I get an error. Could you please provide the huggingface code to load the tokenizer and the model?