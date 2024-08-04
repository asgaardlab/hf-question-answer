## https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/discussions/16

contains_question: yes

question_part: I notice in config.json that the sliding window is set to null. Does this mean that the defacto sliding window is the full embedding input length of 32k? FWIW, running Mistral v0.1 there always seemed to be issues running contexts above the sliding window length (e.g. see this issue), so maybe that's related