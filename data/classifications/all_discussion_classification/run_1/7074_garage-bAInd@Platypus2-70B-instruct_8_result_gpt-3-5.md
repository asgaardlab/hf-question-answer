## https://huggingface.co/garage-bAInd/Platypus2-70B-instruct/discussions/8

contains_question: yes
question_part: Hi, I wonder why do you set `use_cache=False` in [config.json](https://huggingface.co/garage-bAInd/Platypus2-70B-instruct/blob/main/config.json#L24)? As far as I understand, this gives identical results to `use_cache=True` for autoregressive models but runs the O(n^3) generation algorithm instead of the O(n^2) one (i.e., re-runs prefix for generating every new token). I think you can significantly speed up generation for this model by removing this line from the config.