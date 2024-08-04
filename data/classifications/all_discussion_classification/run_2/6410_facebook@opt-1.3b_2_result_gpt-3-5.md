## https://huggingface.co/facebook/opt-1.3b/discussions/2

contains_question: yes

question_part: It seems like the tokenizer for this model is not correct as in I get very bad generation results if I use the tokenizer from OPT-30B model. In my case I am doing in-context learning evaluations and I get expected performance when I use the tokenizer from the 30B model. I am wondering if the tokenizer linked to this model is incorrect as I also see that the 30B model had a fix (https://huggingface.co/facebook/opt-30b/discussions/1) merged that I don't see for this model.