## https://huggingface.co/facebook/esmfold_v1/discussions/3

contains_question: yes

question_part: Why is the special token for padding `A` in `special_tokens_map.json`? It seems like the padding token is `<pad>` in the vocabulary, in the default instantiation of `EsmTokenizer`, etc. Is there a reason for this? It seems strange to add random Alanine's to pad a protein so that the whole batch is of the same size.