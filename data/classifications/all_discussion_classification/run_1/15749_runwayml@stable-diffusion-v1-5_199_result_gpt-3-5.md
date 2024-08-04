## https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/199

contains_question: yes

question_part: With 
`image = pipe(prompt, passes=20, prompt_strength=20, width=160, height=160).images[0]? `
 the model returns a black censored image... 
Is the model too keen to censor everything or are there something in the arguments that forces this?
I am trying to do a matrix of different parameters for reference; if this censorship threshold is this low, I think I have to rethink my tactics?