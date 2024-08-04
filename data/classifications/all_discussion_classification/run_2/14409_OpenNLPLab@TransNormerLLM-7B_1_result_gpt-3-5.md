## https://huggingface.co/OpenNLPLab/TransNormerLLM-7B/discussions/1

contains_question: yes
question_part: Also, `do_eval` in particular is evaluated on every `forward` call for each `NormLinearAttention` layer. Is there a particular reason for this, or should it instead be a global