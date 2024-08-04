## https://huggingface.co/Writer/camel-5b-hf/discussions/5

contains_question: yes

question_part: Can we modify the prompt for camel which is like 

    "Below is an instruction that describes a task."
    "Write a response that adequately completes the request.\n\n"
    "### Instruction:\n{query_str}\n\n### Response:"

To something like 
```
    "Below is an instruction that describes a task."
    "Write a response that adequately completes the request.\n\n"
    "Should not repeat the text in response"
    "### Instruction:\n{query_str}\n\n### Response:"
```