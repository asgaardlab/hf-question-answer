## https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/discussions/70

contains_question: yes
question_part: It looks like SDXL implemented the techniques described in "Common Diffusion Noise Schedules and Sample Steps are Flawed" (https://arxiv.org/pdf/2305.08891.pdf) but I'm unable to replicate the output seen in that paper, specifically "solid black background," with vanilla SDXL and even with the params mentioned in figure 3 of that paper (DDIM, 50 steps, CFG 7.6 and rescale of 0.7). The output is definitely not solid black. Anything I should be changing? Or did I misunderstand that SDXL was using these techniques?