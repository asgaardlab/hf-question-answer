## https://huggingface.co/pere/nb-nn-translation/discussions/1

contains_question: yes
question_part: Hi, very useful model thank you! However I think there is an issue with the `spiece.model` file.  `AutoTokenizer.from_pretrained("pere/nb-nn-translation", use_fast = False)` gives a tokenizer with vocab size 250,100 whereas  `AutoTokenizer.from_pretrained("pere/nb-nn-translation", use_fast = True)` gives a vocab size of 50,003. I believe the latter, which doesn't rely on the sentencepiece model directly, is the correct one. Would you be able to upload the right file? Thanks