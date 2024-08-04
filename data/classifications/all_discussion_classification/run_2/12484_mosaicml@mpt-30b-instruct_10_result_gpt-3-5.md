## https://huggingface.co/mosaicml/mpt-30b-instruct/discussions/10

contains_question: yes

question_part: A simple scenario is given a question and a context, if the answer is not contained within the context, ask for the question to be rephrased. Smaller and simpler models can do this without issue, but MPT fairly consistently answers when the context does not contain the answer, rather than following the instruction. Even if I include that "all previous knowledge should be forgotten" it doesn't seem to keep the model on task. Is there a trick to prompting in this way with MPT?