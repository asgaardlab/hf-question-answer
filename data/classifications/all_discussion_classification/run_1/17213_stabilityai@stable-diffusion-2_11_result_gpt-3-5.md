## https://huggingface.co/stabilityai/stable-diffusion-2/discussions/11

contains_question: yes

question_part: As mentioned on the model card page: "If you have low GPU RAM available, make sure to add a pipe.enable_attention_slicing() after sending it to cuda for less VRAM usage (to the cost of speed)" Which file do I add the  pipe.enable_attention_slicing()  to?