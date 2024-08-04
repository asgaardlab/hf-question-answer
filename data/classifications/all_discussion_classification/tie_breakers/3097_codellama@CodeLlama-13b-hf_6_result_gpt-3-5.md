## https://huggingface.co/codellama/CodeLlama-13b-hf/discussions/6

contains_question: yes

question_part: The `special_tokens_map.json` is missing the extra 16 tokens. I believe at least we need `<PRE>`, `<MID>`, `<SUF>` defined there for infilling.