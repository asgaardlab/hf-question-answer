## https://huggingface.co/google/flan-t5-xxl/discussions/29

contains_question: yes

question_part: I saw that this activates greedy generation mode in <a href="https://github.com/huggingface/transformers/blob/23c146c38b42d1193849fbd6f2943bf754b7c428/src/transformers/generation/utils.py#L1090">this function</a>. However, the paper https://openreview.net/pdf?id=gEZrGCozdqR has many more usages of top-k sampling than greedy sampling. Shouldn't the default be top-k sampling?