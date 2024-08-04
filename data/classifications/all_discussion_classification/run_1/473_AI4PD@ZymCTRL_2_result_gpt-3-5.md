## https://huggingface.co/AI4PD/ZymCTRL/discussions/2

contains_question: yes

question_part: 
Q1. For fine-tuning (Example 2), is there a minimum memory requirement in GPU? In the ZymCTRL paper, Nvidia A100 GPUs with 40GB memory were used. My GUS has 12GB memory, wondering if it matters. Since I got the same error https://discuss.huggingface.co/t/cuda-out-of-memory-error/17959/4 Reduced batch size to 1, as well as block size down to 32, but still got the same error. If I used CPU instead with --no_cuda, I could fine-tune albeit a way long time. 

Q2. Does it make sense to fine-tune the pretrained ZymCTRL with a custom tokenizer (in which smiles strings are tokenized, instead of EC numbers)? In general, any restriction on the length of prompts in the train set?