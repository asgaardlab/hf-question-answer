## https://huggingface.co/stabilityai/stablelm-zephyr-3b/discussions/4

contains_question: yes

question_part: Since this model was trained on HuggingFaceH4/ultrafeedback_binarized and Allen AI has shown that the dataset suffers from TruthfulQA contamination, is it safe to conclude that this model is also subject to this contamination, or did you filter out specific entries during training? If it is indeed trained on the contaminated dataset, can we expect a v2 with it trained on the clean dataset, such as allenai/ultrafeedback_binarized_cleaned or argilla/ultrafeedback-binarized-preferences-cleaned