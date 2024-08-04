## https://huggingface.co/CompVis/stable-diffusion-v-1-3-original/discussions/9

contains_question: yes  
question_part: Hey everyone, in the Discord when you generate multiple samples, the bot tells you the seed for each image. However, in txt2img.py, it seems like seed_everything just has one seed for all of the samples. For example, if you do --n_samples=3, how do you get a separate seed for each image