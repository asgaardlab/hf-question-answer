## https://huggingface.co/CarperAI/stable-vicuna-13b-delta/discussions/1

contains_question: yes

question_part: 
I've not seen a model with that layout before. Is it correct that BOS, EOS and UNK are all the same?
Is that a requirement for this model? And if so, is that why the `special_tokens_map.json` is like that?
Or maybe given `skip_special_tokens=True` is set, `special_tokens_map.json` isn't even used?
Reason I ask is this will have implications for people doing inference in eg text-generation-webui. It has an option to "skip special tokens" but the user needs to know to set that, if it's required.
And if they're not going to set that, it does seem odd to me that BOS and EOS would be the same.
So it'd be awesome to get some clarification on that.