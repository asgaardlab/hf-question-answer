## https://huggingface.co/bigscience/bloom/discussions/234

contains_question: yes

question_part: ## Question. 
Thinking that tokenized prompt as the 'input_ids' and tokenized summary as 'labels' as the training data to the model as below but not sure this is a correct approach or not. Please advise if this works, beyond all, if Trainer is fit for purpose.

DataCollatorWithPadding class does not pad the 'labels' element, which causes an error at train(). Hence used padding at tokenizer to pad labels but not sure this is correct. Please advise if there is another way to manage labels.

Please also give correction/suggestion if any.