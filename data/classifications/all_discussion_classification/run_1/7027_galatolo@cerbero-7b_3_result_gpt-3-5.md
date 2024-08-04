## https://huggingface.co/galatolo/cerbero-7b/discussions/3

contains_question: yes

question_part: Why is it so slow, even on GPU
I'm comparing Cerbero 7B to Llama2 /B.
Even if I'm using a 2 A10 GPU VM Cerbero is surprisingly slow. I have checked (gpustat) it is running on GPU... but getting an answer takes minutes.
Is it a fine tuning of Mistral 7B or do we have architectural changes requiring much more computing power