## https://huggingface.co/CompVis/stable-diffusion-v1-4/discussions/52

contains_question: yes

question_part: To allow for changing the image size and still getting similar images, it would be an interesting idea to copy the initialization from a smaller image to a larger when re-rendering to get similar results in the area where the noise was copied. One could also try to scale the noise, but I wonder if this would result in blocky images.