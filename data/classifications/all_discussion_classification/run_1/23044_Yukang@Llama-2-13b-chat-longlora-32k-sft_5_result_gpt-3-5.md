## https://huggingface.co/Yukang/Llama-2-13b-chat-longlora-32k-sft/discussions/5

contains_question: yes  
question_part: Since this has a predefined scaling factor, would it be possible to update the config.json to reflect the definition as used by vLLM? e.g. `"rope_scaling": {"factor": 8.0, "type": "linear"},` as opposed to `null`