## https://huggingface.co/jondurbin/airoboros-7b-gpt4-1.2/discussions/3

contains_question: yes
question_part: Hey I'm a little confused, in textgen webui and the vicuna docs the Vicuna-1.1 prompt format seems to be like this:
"A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.

USER: prompt
ASSISTANT:"

but your model card has it all in a single line without any newlines. So I just wanna double check that the correct prompt for this model should not have those newlines that the Vicuna 1.1 does, and just be separated by spaces in one line instead?