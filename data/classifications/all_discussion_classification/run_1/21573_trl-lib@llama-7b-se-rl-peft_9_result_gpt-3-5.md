## https://huggingface.co/trl-lib/llama-7b-se-rl-peft/discussions/9

contains_question: yes

question_part: Hello, thanks for contributing this amazing model. When I try and laod it using:

from transformers = AutoModel
model = AutoModel.from_pretrained("trl-lib/llama-7b-se-rl-peft")

I get the following error:

OSError: trl-lib/llama-7b-se-rl-peft does not appear to have a file named config.json. Checkout 'https://huggingface.co/trl-lib/llama-7b-se-rl-peft/main' for available files.

Is there perhaps an intermediary step I need to carry out before loading the model?