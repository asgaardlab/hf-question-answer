## https://huggingface.co/google/flan-t5-xxl/discussions/29

contains_question: yes  
question_part: However, the paper https://openreview.net/pdf?id=gEZrGCozdqR has many more usages of top-k sampling than greedy sampling. Shouldn't the default be top-k sampling? (more generally, I'm curious about what the best practices for sampling from SOTA LLMs is. It seems that top-p nucleus sampling is the most common, but beam search and greedy seem also used, and the articles online don't mention **which** models use each of them)