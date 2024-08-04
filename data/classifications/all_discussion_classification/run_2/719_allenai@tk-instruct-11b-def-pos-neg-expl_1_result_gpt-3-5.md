## https://huggingface.co/allenai/tk-instruct-11b-def-pos-neg-expl/discussions/1

contains_question: yes
question_part: 2.) The tokenizer, as described by the model card, ignores newlines and certain whitespaces. I think that those whitespaces are necessary in order to follow the input template as described by the tk-instruct paper. How do we change the tokenizer.encode such that it does not ignore whitespace?