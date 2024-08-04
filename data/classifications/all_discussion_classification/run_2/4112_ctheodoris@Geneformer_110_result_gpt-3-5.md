## https://huggingface.co/ctheodoris/Geneformer/discussions/110

contains_question: yes

question_part: Do you have any suggestions for updating the pre-trained model without a down-stream task? Would it be legit to use `BertForMaskedLM.from_pretrained(<path to your pretrained model>)` and continue training it on a new dataset? Which datacollator should I use?