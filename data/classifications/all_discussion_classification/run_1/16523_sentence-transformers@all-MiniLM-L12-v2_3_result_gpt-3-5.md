## https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2/discussions/3

contains_question: yes
question_part: Recently i notice the default max sequence length of it is 128, while on the page it says max sequence length is 256. However on the lower part of the page, it says the model was trained with 128 token length. So i'm not sure if it's ok to increase token length to 256, will this decrease the quality of vector because hyper parameters were trained with 128 token length? And since it's in sentence-transformer library, max_sequence_length can even be set as 512. Can I also do this for this model?