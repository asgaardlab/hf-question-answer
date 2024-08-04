## https://huggingface.co/stabilityai/stable-diffusion-2-1/discussions/40

contains_question: yes
question_part: Still I do get the inferenced image as 512x512 since vae_decoder takes latents input of shape 512x512 and that results in a pixelated image. What are the shapes used for the above three nodes for proper inferencing
With these inputs the output was proper for SD1.4 models also tried using the `DPMSolverMultistepScheduler` for SD2.1 still the output is the same.
Saw somewhere the encoder_hidden_states blob shape was updated ? What are the right dimensions to be used