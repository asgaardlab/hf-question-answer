## https://huggingface.co/notstoic/pygmalion-13b-4bit-128g/discussions/6

contains_question: yes

question_part: I was under the impression that setting use_safetensors=True should instruct the from_pretrained() method to load the model from the safetensors format. However, it appears the method is searching for the usual model file formats (pytorch_model.bin, tf_model.h5, etc) instead of recognizing the safetensors format.