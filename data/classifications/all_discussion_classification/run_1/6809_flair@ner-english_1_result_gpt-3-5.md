## https://huggingface.co/flair/ner-english/discussions/1

contains_question: yes
question_part: How can I use it for NER training?
Is it simply taking the token embeddings from 'xlm-roberta-large' and puts a linear layer for NER on top of it?
Where exactly FLERT's functionalities are used? Are they automatically handled behind the scenes?
Any suggestions on whether or not we should use CRF layer on top of bert embeddings for NER tasks
The flag "use_rnn" what exactly it does? If I switch it off, what does it do? Will it switch off char-rnn layer or word-rnn layer?