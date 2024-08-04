## https://huggingface.co/CarperAI/stable-vicuna-13b-delta/discussions/1

contains_question: yes

question_part: I just did the merge and noticed that special_tokens_map.json contains this:
```
{
  "bos_token": "</s>",
  "eos_token": "</s>",
  "pad_token": "[PAD]",
  "unk_token": "</s>"
}
```
I've not seen a model with that layout before. Is it correct that BOS, EOS and UNK are all the same? 
And relatedly, I see in your README example that you do inference with `skip_special_tokens=True`: