## https://huggingface.co/Yukang/LongAlpaca-13B/discussions/1

contains_question: yes

question_part:
2) There seems to be an issue with the tokenizer in this repo. It doesn't load smoothly.
``` 
ValueError: Couldn't instantiate the backend tokenizer from one of:
(1) a `tokenizers` library serialization file,
(2) a slow tokenizer instance to convert or
(3) an equivalent slow tokenizer class to instantiate and convert.
You need to have sentencepiece installed to convert a slow tokenizer to a fast one.
```