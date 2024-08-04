## https://huggingface.co/ai4bharat/indic-bert/discussions/2

contains_question: yes

question_part: The fifth "word" appears to be a non-spacing Candrabindu mark by itself.    If I feed the words to the indic-bert tokenizer word by word, I would expect it to produce <UNK> or something similar for an untokenizable word such as that.  Instead, it produces nothing.  Is that expected behavior I should compensate for, or is it something that can be fixed in the tokenizer?