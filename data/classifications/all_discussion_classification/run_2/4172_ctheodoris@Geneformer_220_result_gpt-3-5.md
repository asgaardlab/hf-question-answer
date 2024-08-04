## https://huggingface.co/ctheodoris/Geneformer/discussions/220

contains_question: yes

question_part: Hi Christina! Thank you for the amazing work. I have two questions.
First, regarding the downstream task like cell-type classification, the dataset need to be split into training set and testing set for finetuning and predicting respectively. When tokenizing the data using tk.tokenize_data, there are two methods:
1, tokenize the whole data and then split them;
2, split them and then tokenize them.
Are they different in the generated results?