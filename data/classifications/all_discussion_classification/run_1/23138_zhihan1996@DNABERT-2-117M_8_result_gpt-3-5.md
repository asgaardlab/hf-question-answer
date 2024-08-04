## https://huggingface.co/zhihan1996/DNABERT-2-117M/discussions/8

contains_question: yes

question_part: I am trying to extract hidden layer output from all the layers in the model. As per the documentation, the **`output_all_encoded_layers`: boolean which controls the content of the `encoded_layers` output as described below. Default: `True`.**. However Line 586 (https://huggingface.co/zhihan1996/DNABERT-2-117M/blob/main/bert_layers.py#L586) has this set to `False`, which I was expecting to be the case in contrast to what documentation says because only last layer was returned in the output. However, when I set it to `True` the inference fails. The traceback is as follows: