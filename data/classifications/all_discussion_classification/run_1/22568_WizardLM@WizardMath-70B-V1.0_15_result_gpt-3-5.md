## https://huggingface.co/WizardLM/WizardMath-70B-V1.0/discussions/15

contains_question: yes

question_part: I noticed inside the config that `"max_position_embeddings": 2048,"`. The base 70b model has a 4096 token length (see https://huggingface.co/meta-llama/Llama-2-70b-chat-hf/blob/main/config.json). Was this intentionally reduced?