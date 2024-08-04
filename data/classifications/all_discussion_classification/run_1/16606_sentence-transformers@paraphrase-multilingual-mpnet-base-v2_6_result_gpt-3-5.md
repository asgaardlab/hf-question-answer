## https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2/discussions/6

contains_question: yes  
question_part: Is this on purpose or is it an error in the tokenizer configuration for transformers version? I would suggest updating the transformers example code in the Readme at last to give a hint about this. Getting different "default" results for the same model can cause some confusion.  
Additional question: Why is the max. input sequence set to 128 tokens at default with sentence_transformers at all when the architecture can support longer sequences?