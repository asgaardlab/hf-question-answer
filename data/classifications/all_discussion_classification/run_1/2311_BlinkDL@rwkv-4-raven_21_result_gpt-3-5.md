## https://huggingface.co/BlinkDL/rwkv-4-raven/discussions/21

contains_question: yes

question_part: 
- 1. Is it possible to share the resources you used when you train the 7B model
- 2. How can I set the accumulate_grad_batches in train.py scripts. I find this in my log file but I can't set it...
- 3. I notice one phenomenon when I fine-tuned model with LoRA (actually w/o LoRA is same when I train a 1B5 model), at the beginning of training, they will occupy around 42GB CPU memory only, then split data into CPU and GPU memory separately, is it normal? 
- 4. What is the meaning of grad_cp, is it mean we will compute the gradient again, so we won't save it in GPU memory (but computation time is 30% lower), save around 7G for 7B model? (7G is estimated by me, may not be correct.)