## https://huggingface.co/stabilityai/stable-diffusion-2/discussions/49

contains_question: yes

question_part: I encountered a memory leak problem. Whether we load the model to gpu or delete the model with del and do gc, the memory is not recycled. The ideal case for us is that the memory usage goes back to exactly the original value after the load model -> del model -> gc process.
Therefore, what should I do to reclaim the memory occupied by the stable diffusion model.