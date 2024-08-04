## https://huggingface.co/PygmalionAI/pygmalion-7b/discussions/8

contains_question: yes
question_part: I've been trying to quantize this down to 4 bits for the last day-ish, and it looks like it loses touch with the tokens that are being output. (_It outputs at a cadence that suggests it is predicting tokens, but the tokens are nonsense._) This is my first time trying to quantize a HuggingFace Transformers model. (I've done it in the past with the raw LLaMA model using `llama.cpp`.) Any pointers that I could use to figure out what's going wrong?