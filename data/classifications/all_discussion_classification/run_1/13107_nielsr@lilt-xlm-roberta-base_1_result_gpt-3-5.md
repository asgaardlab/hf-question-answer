## https://huggingface.co/nielsr/lilt-xlm-roberta-base/discussions/1

contains_question: yes
question_part: I am getting the following error - 
TypeError: _batch_encode_plus() got an unexpected keyword argument 'boxes' when trying to encode the dataset using following command- encoding = processor(words, boxes=boxes, word_labels=word_labels, truncation=True, padding="max_length") I have created a pipeline which works with lilt-roberta-base model and was trying to use the same pipeline with the lilt-xlm-roberta-base model. Ideally shouldn't the same code for nielsr/lilt-xlm-roberta-base and SCUT-DLVCLab/lilt-roberta-en-base. My understanding is we have removed the roberta-base with the xlm-roberta. But still shouldn't the model use bounding boxes for processing. Am I missing anything?