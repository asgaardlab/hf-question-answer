## https://huggingface.co/allenai/scibert_scivocab_cased/discussions/5

contains_question: yes

question_part: In the example below, the last few words are about an URL, which should not be put into different subwords. However, the tokenizer chopped the URL. 
I wonder if this is because I am not handlling it correctly, or scibert behaves incorrectly, or it's unevitable problem in bert tokenization.