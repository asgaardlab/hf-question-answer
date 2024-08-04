## https://huggingface.co/bigscience/bloomz-7b1/discussions/6

contains_question: yes

question_part: Should the bloomz-7b1 tokenizer_config.json have padding_side="left"?
The other bloom tokenizers seem to set that, and running generation with 7b1 shows this message:

``` 
A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer. 
```