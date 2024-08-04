## https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/71

contains_question: yes

question_part: I have encountered a memory leak problem, we need to store and switch the model of stable diffusion in memory, but when we convert the model in memory to gpu, the memory is not reclaimed, and at the same time, when the model in memory is deleted, the memory also not recycled.
Therefore, what should I do to reclaim the memory occupied by the stable diffusion model.