## https://huggingface.co/BlinkDL/rwkv-4-raven/discussions/14

contains_question: yes

question_part: At the moment, I am experimenting with dynamic INT4 quantization of your pre-trained models, however, it made me think: maybe we can natively train at least one decently sized model fully in INT4? Or, at least, use the existing model as a "teacher" and make it train a quantized "student" model.