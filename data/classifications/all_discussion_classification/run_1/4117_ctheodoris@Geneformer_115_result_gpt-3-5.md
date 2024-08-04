## https://huggingface.co/ctheodoris/Geneformer/discussions/115

contains_question: yes

question_part: For pretraining a new model from scratch with a new pretraining corpus other than Genecorpus-30M, if the memory for the device is not enough for the large dataset, could I split the dataset into multiple parts and generate a .loom file for each part. And then, tokenize each .loom file to a .arrow file. Finally merge those .arrow files into one .arrow file with the help of Dataset.concatenate_datasets. Is that correct