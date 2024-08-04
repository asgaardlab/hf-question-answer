## https://huggingface.co/HuggingFaceM4/idefics-9b-instruct/discussions/7

contains_question: yes  
question_part: I have also tried to reproduce it on my server with 8x NVIDIA RTX A6000. With the exact same code from the notebook I receive the exact same output: 'Question: What's on the picture? Answer: Kittens.'  

The only difference between the colab code and my code is the removal of `quantization_config=bnb_config` from the `IdeficsForVisionText2Text.from_pretrained(...)` parameter list. I have had a colleague find their own way of running the model with the code you provided and they have reproduced the exact same issue independently (`Question: What's on the picture? Answer:`).