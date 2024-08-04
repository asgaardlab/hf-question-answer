## https://huggingface.co/teknium/Phi-Hermes-1.3B/discussions/4

contains_question: yes

question_part: Since at fp16 it takes only 3.16 GB VRAM for inferencing Phi 1.5, can we run 24 copies (approximately) of Phi 1.5 on an A100-80GB GPU?
If that is possible and 3ms per token (as claimed in Phi 1.5 technical paper) is also achievable with flash attention - can we generate 7200 tokens (24 copies × 300 tokens per second) per second on a A100-80GB GPU?