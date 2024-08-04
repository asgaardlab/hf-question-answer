## https://huggingface.co/facebook/opt-125m/discussions/18

contains_question: yes

question_part: In the model configuration for this (and other opt models) the vocab_size is 50272, but the tokenizer has vocab size 50265, which matches the original vocabulary [here](https://github.com/facebookresearch/metaseq/blob/main/projects/OPT/assets/gpt2-vocab.json). and the one on huggingface [here](https://huggingface.co/patrickvonplaten/opt-30b/tree/main). Could this be updated somehow (although I realise that could mess with checkpoints etc.)? There's [this](https://github.com/huggingface/transformers/issues/18268) issue on the transformers github referencing the samething.