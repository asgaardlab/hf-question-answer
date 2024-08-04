## https://huggingface.co/LeoLM/leo-hessianai-70b-chat/discussions/4

contains_question: yes

question_part: i get the error: (model has 32128, but models/LionM-70B/tokenizer.model has 32000) when trying to convert the model to FP16 format before quantization. This seems to be a mismatch between the used tokenizer and the config.json. An easy fix is to just set the  "vocab_size" parameter to 32000, however, this results inn problems further down the line, when quantizing. Any suggestions