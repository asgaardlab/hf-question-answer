## https://huggingface.co/ctheodoris/Geneformer/discussions/227

contains_question: yes

question_part: I see from your code that the model actually has only PAD and MASK two special tokens for MLM pretraining, but when it comes to the  downstream cell type annotation task, the used classifier in BertForSequenceClassification is actually get the first token of the hidden states, since you have no CLS token, so you actually use the first gene to represent the cell embedding for cell type annotation task