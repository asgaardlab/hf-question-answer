## https://huggingface.co/Norquinal/llama-2-7b-claude-chat-rp/discussions/1

contains_question: yes
question_part: Thrown during validation:
`do_sample` is set to `False`. However, `temperature` is set to `0.9` -- this flag is only used in sample-based generation modes. 
You should set `do_sample=True` or unset `temperature`.