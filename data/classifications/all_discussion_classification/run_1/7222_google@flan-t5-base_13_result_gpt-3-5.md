## https://huggingface.co/google/flan-t5-base/discussions/13

contains_question: yes

question_part: It should work but I got this error: RuntimeError Traceback (most recent call last) in 5 # Prepare labels 6 labels = inputs.clone() ----> 7 labels[0, :-1] = labels[0, 1:]