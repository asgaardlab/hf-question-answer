## https://huggingface.co/naxautify/gpt2-4k/discussions/2

contains_question: yes

question_part: 
* Fine-tune GPT2 or train from scratch? (AFAICT it's challenging to fine-tune w/ different n_ctx than a base model)
* What trainer?
* I'm seeing the weights tensor have a dim of [2048,768] rather than the expected [4096,768] for "gpt2-4k"; is this a -2k context gpt2?
* Should n_ctx/n_positions in config.json be updated?