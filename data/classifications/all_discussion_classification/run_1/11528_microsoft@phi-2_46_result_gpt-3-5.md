## https://huggingface.co/microsoft/phi-2/discussions/46

contains_question: yes

question_part: Specifically, when I input commands like "Print all primes between 1 and n", the model continues generating output until it reaches the maximum length limit. I attempted to use the eos_token_id=tokenizer.eos_token_id parameter to signal the end of the sequence, but it hasn't resolved the issue. Could someone guide me on how to make the model stop generating once it reaches a logical conclusion, instead of continuing until the max_length?