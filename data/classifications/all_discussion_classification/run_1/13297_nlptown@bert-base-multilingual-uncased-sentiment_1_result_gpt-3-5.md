## https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment/discussions/1

contains_question: yes

question_part: I have tried to load the file tf_model.h5 by using tf.keras.models.load_model('tf_model.h5'). However, this gave me this error: 'ValueError: No model config found in the file at ...' Online I found that this error could mean that only the weights were saved and not the entire model. Does someone have a solution for this