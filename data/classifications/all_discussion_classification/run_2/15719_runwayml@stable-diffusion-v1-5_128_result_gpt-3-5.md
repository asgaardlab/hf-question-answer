## https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/128

contains_question: yes
question_part: I have a question, during the training of diffusion, if it is a conditional input, (for example, an image generation model that combines text) it seems that the crossattention in the network does not use the window attention similar to the swing transformer structure, but directly uses the global attention. Considering that the size of the input image is 512*512, is this the reason why diffusion is so difficult to train?
I don't know if my understanding is correct or not, I hope for your answers.