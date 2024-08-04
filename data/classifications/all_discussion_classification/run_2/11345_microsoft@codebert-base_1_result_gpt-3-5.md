## https://huggingface.co/microsoft/codebert-base/discussions/1

contains_question: yes

question_part: I was experimenting with the model when I noticed that the tokenizer vocab contains tokens that don't really make sense for a code model (e.g. full tokens for "embarrassed" and "fossils" and "Hermione"). Upon closer inspection, it seems the tokenizer `roberta-base` tokenizer. In case this was by design, why was the tokenizer not trained on the training data?