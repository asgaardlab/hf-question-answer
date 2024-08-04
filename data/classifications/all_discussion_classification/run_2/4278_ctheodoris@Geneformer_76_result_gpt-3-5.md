## https://huggingface.co/ctheodoris/Geneformer/discussions/76

contains_question: yes

question_part: i have a single cell dataset(e.g. 500 cells * 3000 genes ). How can i get gene embedding using your pretrained model. You mentioned this documentation( https://huggingface.co/docs/transformers/main_classes/output ) in other discussion,but how can i tokenizer my genes as inputs ? i found you provided "TranscriptomeTokenizer", but the output(xxx.dataset) can not be directly input to the model (outputs = model(**inputs, labels=labels))