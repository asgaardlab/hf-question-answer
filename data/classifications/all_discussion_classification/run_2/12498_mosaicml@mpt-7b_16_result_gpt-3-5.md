## https://huggingface.co/mosaicml/mpt-7b/discussions/16

contains_question: yes

question_part: My graphics card is barely sufficient (GTX1080 TI with 8GB VRAM).  But thanks to ``llm_foundary`` GitHub repository, I was able to discern which blocks needed split-locking on the accelerator, and expand all that out manually and tie the weights so it works on a home PC with a crappy graphics card via:  https://huggingface.co/docs/accelerate/usage_guides/big_modeling .  It runs at about 1.09 it/s (a token a second on a home computer 😅🔥) -- My brave little toaster did it so yours can, too.