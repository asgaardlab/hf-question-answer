## https://huggingface.co/HuggingFaceM4/idefics-9b-instruct/discussions/7

contains_question: yes
question_part: I have been running your [Colab](https://github.com/huggingface/notebooks/blob/main/examples/idefics/finetune_image_captioning_peft.ipynb) notebook and it works like a charm on Google Colab. I have also tried to reproduce it on my server with 8x NVIDIA RTX A6000. With the exact same code from the notebook I receive the exact same output: `Question: What's on the picture? Answer: Kittens.` But whatever I do, if I do not use the quantised model but `idefics-9b` or `idefics-9b-instruct`, I only ever receive: `Question: What's on the picture? Answer:` The only difference between the colab code and my code is the removal of `quantization_config=bnb_config` from the `IdeficsForVisionText2Text.from_pretrained(...)` parameter list. I have a had a colleague find their own way of running the model with the code you provided and they have reproduced the exact same issue independently (`Question: What's on the picture? Answer:`). I've tried different GPUs and different servers, but without the quantised model, I am unable to produce any output. The model loads into memory and is accessed during inference - it just does not generate or return or display any new tokens (I have also increased `max_new_tokens=50`, tried other prompts like the Pokémon example).