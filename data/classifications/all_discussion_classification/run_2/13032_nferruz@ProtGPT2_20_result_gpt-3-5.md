## https://huggingface.co/nferruz/ProtGPT2/discussions/20

contains_question: yes

question_part:  I am wondering how the model inserts newline(\n) characters into the generated sequences. It seems that a newline character is inserted after every 60 characters to mimic the format of a typical text document. However, in some cases, the model inserts a new line before 60 characters. 
I couldn't find a proper answer to these questions:
- Are there any criteria for inserting newline characters into sequences? 
- Are "\n" only used for formatting purposes and can it be removed to obtain the actual amino acid sequence?