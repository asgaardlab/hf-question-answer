## https://huggingface.co/CompVis/stable-diffusion-v1-4/discussions/43

contains_question: yes

question_part: 

What's the difference between latent or pipe generator manual seeding? I just did some experiments and if I add only the generator to the latents with the same manual seed, still different results in images show up, but if I add the generator directly to the pipe, the image stays the same. Now, the question is, how can the image change if the latents are the same (same seed)? Is this intended behavior?

Why pytorch lightning's seed_everything() (which works as intended btw) allow only a lower random number in the generator? Will the generator given number down casted to fit the pytorch lightning random seed? 

Keeping the latents in the same dimensions with the same global seed while changing the width and height of the image will change the result. How do the imposed noise changes on image dimension change?