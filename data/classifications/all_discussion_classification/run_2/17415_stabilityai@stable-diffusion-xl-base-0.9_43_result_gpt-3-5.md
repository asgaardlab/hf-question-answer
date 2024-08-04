## https://huggingface.co/stabilityai/stable-diffusion-xl-base-0.9/discussions/43

contains_question: yes

question_part: The API calls are not working using any method. The Host API on the Model gives the same error as the gr.Interface method. And Response/Query method says the BytesIO file is unreadable... Both methods work when tested with SD 2.1, so it isn't my code. Plus, no one else has it running... You need to actually add the StableDiffusionXLPipeline, it simply doesn't exist... Thus no one can do API right now from HF.