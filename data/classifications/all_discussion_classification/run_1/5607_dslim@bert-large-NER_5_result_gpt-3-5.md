## https://huggingface.co/dslim/bert-large-NER/discussions/5

contains_question: yes

question_part: How did you deal with the misalignment that appears after tokenization between the tokens and the ner tags? If the word "Japan" has as ner tag "B-LOC", how does it look like after it is tokenized as follows: "JA", "#PA", "#N"? Do you for example re-align the ner tags as "B-LOC", "I-LOC", "I-LOC"? In the calculation of these metrics, do we also evaluate the performance on the "O" label?