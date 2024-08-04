## https://huggingface.co/alirezamsh/small100/discussions/7

contains_question: yes

question_part: Hi! I used the Small100Tokenizer for some experiments a couple of weeks ago and it worked perfectly fine, but when I tried to rerun it more recently it resulted in an attribute error ('AttributeError: 'SMALL100Tokenizer' object has no attribute 'encoder''). I encountered the same error when using the demo link on the model card. After switching to the M2MTokenizer (M2M100Tokenizer.from_pretrained("alirezamsh/small100")) it ran smoothly – does anybody know what the issue could be?