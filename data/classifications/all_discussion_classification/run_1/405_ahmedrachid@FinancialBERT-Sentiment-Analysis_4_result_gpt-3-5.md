## https://huggingface.co/ahmedrachid/FinancialBERT-Sentiment-Analysis/discussions/4

contains_question: yes

question_part: Does the program support num_labels = 2? Thank you for the excellent work!! Is there a way to set num_labels = 2? I tried to modify the codes here in order to accommodate 2 labels (positive, negative) rather than 3 (positive, neutral, negative) as follows: "model = BertForSequenceClassification.from_pretrained("ahmedrachid/FinancialBERT-Sentiment-Analysis",num_labels=2)" but I got an error message.