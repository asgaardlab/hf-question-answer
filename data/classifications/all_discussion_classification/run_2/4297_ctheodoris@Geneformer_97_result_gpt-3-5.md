## https://huggingface.co/ctheodoris/Geneformer/discussions/97

contains_question: yes

question_part: First question is regarding the tokenizer - can you give a bit more detailed explanation how it works. My understanding is that it takes cell sequence and assigns ids based on which genes have been expressed in this sequence. Is that correct? Does the score of how much is gene expressed play a role and how? 

question_part: However, if I have a set of genes with some feature, and set of genes that do not express same feature, can I use geneformer's method to predict on the bigger set of genes which will have a given feature? Or it is not possible and I can only work within boundaries of gene/token classification within gene or cell classification? 

question_part: Also, one question I have, since in cell sequences, the ordering of genes that are expressed does not really matter, at least not as in text, what is the intuition based on which token classification of genes would work?