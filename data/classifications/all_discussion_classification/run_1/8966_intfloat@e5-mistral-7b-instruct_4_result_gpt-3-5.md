## https://huggingface.co/intfloat/e5-mistral-7b-instruct/discussions/4

contains_question: yes

question_part: In the code example, you measure the similarity between two sentences with the inner product between normalized embeddings. However, in Section 3.2 of your technical report, you wrote "In this paper, we adopt the temperature-scaled cosine similarity function as follows".

I have two sets of documents in my use case, denoted A and B. The task is to find the top-k documents in B that are most semantically similar to those in A (by computing the average distance between each document in B and all documents in A). What do you recommend me to do to use as a distance measure between two embeddings, traditional cosine distance, or the temperature-scaled cosine similarity function?

As a bonus question, do you think it would be better if I prepend the instructions to documents in A in addition to those in B, i.e. prepend them to documents in addition to queries? After all, this is a symmetric task, and I suppose some symmetry will help.