## https://huggingface.co/llava-hf/llava-1.5-7b-hf/discussions/9

contains_question: yes

question_part: Even if I batch the images `outputs = pipe(imgs, prompt=prompt, generate_kwargs={"max_new_tokens": 200})` I am note getting much of a speedup (i.e. for 4 images it takes ~28 seconds). Are there any other way to speed up text generation?