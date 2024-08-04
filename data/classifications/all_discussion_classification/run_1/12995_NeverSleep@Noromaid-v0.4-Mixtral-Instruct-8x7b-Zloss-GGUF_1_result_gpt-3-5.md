## https://huggingface.co/NeverSleep/Noromaid-v0.4-Mixtral-Instruct-8x7b-Zloss-GGUF/discussions/1

contains_question: yes

question_part: What's the word on k-quants? 
What was the story there? Bug with llama.cpp's inference or bug with the GGUF quantisation in the first place? 
...was there a bug at all?
p.s. did you keep the original output tensors? if you did I might get the Q8_0 (isn't this also technically a k-quant now?) and re-quantize it down to Q4_K_S or Q3_K_L. 24 GB sweet spot right?
maybe I should just bite the bullet and see if I can QUIP# or HQQ one of these?