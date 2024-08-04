## https://huggingface.co/bigscience/bloom/discussions/132

contains_question: yes

question_part: How does hugging face have so many hosted apis running at once? It is literally a hundred thousand or even more models hosted. Do they load the models when needed, taking turns using available resources? If I were to have only Bloom loaded would there be a significant reduction in the time it takes to get a result vs through the hosted api? Also are many requests coming in concurrently to the model in the hosted api, slowing it down or are requests rare in the hosted api?