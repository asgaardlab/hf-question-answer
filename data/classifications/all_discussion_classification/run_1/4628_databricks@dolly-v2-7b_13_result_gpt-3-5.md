## https://huggingface.co/databricks/dolly-v2-7b/discussions/13

contains_question: yes

question_part: Based on the pipeline.py script I found it's clear that it was close to this format:
INSTRUCTION_KEY = "### Instruction:"
RESPONSE_KEY = "### Response:"
END_KEY = "### End"
But the databricks-dolly-15k dataset used frequently adds a context, how exactly is that incorporated into the chunk of text when you fine tuned this model ?