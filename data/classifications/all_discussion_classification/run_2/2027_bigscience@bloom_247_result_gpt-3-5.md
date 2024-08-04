## https://huggingface.co/bigscience/bloom/discussions/247

contains_question: yes

question_part: am using bloom with Langchain, initialized with temp=1e-10. I am using a FewShotPromptTemplate with 4 examples. It is doing an ok job but truncates the output at a random point. When I initialize with max_tokens, it gives the full string but fills up the balance of the output with arbitrary characters. Anyone else seen this happen and has a solution