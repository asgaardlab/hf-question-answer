## https://huggingface.co/stabilityai/stable-zero123/discussions/8

contains_question: yes

question_part: A few questions here:
- How is it allocated roughly 22gigs even though my gpu only has 10. Does RAM count into that?
- Would changing that allocation fix the error, even though it'd slow down the generation? If so, where would the PyTorch configs be to change that?
- i saw that there is the keyword "train" in the command. Does it actually train the NN or does it make the NN produce 3d images/meshes/files from the 2d images provided? If it is only for training, would i have to use the ckpt like the Stable Diffusion one(or the safetensors) and put it in some kind of WebUI?