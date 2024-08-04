## https://huggingface.co/bullmount/it_nerIta_trf/discussions/2

contains_question: yes

question_part: But I can't figure out which one case I am in and whether this can cause problems in training: - This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model) - This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model)