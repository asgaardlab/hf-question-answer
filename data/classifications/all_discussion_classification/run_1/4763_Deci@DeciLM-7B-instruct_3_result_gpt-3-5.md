## https://huggingface.co/Deci/DeciLM-7B-instruct/discussions/3

contains_question: yes

question_part: I am opening this discussion because I know the prompt format is like following:
```
### System:
{system}
### User:
{usr}
### Assistant:
```
But it would be fantastic if you can add the chat template to the `tokenizer_config.json` as many other models do.  [Here](https://huggingface.co/openchat/openchat_3.5/blob/main/tokenizer_config.json#L51) is an example what I mean.