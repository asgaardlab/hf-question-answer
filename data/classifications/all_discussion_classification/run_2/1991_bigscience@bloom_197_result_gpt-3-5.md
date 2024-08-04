## https://huggingface.co/bigscience/bloom/discussions/197

contains_question: yes

question_part: I wanted to know the hardware requirements for 
a. just running this model 
b. for fine-tuning. 
I want to use it to convert sentences to mathematical expressions. Although the model is able to do that already. I have tried using the hosted API here on hugging face. I wanted to know how can I fine-tune it such that whenever I pass in a sentence it gives me back the expression, without having to tell it what to do. 

Can someone also help me with the following, please?
1.  Guide to fine-tuning, including information on dataset format, loading the dataset, etc.
2. Since the model is autoregressive can I give it a prompt like this 
"
1. sentence: expression
2. sentence: expression
Using the above examples as reference convert the following sentences to expressions:
sentence: 
"
I want to save the model at this point and then later just pass the sentence I want. is this possible? if yes what will be the compute required?