## https://huggingface.co/jbochi/madlad400-3b-mt/discussions/5

contains_question: yes

question_part: The code used to create the tokenizer adds 100 extra tokens by default. The padding token for `T5Tokenizer` is "\<pad\>" by default, which doesn't exist in the sentencepiece model, thus adding another extra token, making batch inference impossible.