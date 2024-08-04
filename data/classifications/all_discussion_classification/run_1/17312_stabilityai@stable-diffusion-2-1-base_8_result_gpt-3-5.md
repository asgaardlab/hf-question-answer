## https://huggingface.co/stabilityai/stable-diffusion-2-1-base/discussions/8

contains_question: yes

question_part: Hi, Im having trouble finding a CLIPModel checkpoint (or just the CLIPVisionModel) that matches the CLIPTextModel used in this version. The open-clip library provides a different interface (not using the CLIPVisionModel class). Other CLIPModel  checkpoint do not match the projection dim of this version (1024, while other checkpoints here are 768 or 512).  Does anyone has a solution or can refer me to the correct checkpoint?