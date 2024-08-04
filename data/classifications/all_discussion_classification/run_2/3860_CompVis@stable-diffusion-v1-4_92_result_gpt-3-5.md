## https://huggingface.co/CompVis/stable-diffusion-v1-4/discussions/92

contains_question: yes

question_part: My questions are:
1.  What does the scheduler do? Why not directly subtract the noise predicted after each inference step from the latent?
2. Among these 4 parts, which are the ones that you trained? The notebook says the text encoder is off-the-shelf. I guess the latent UNet is trained. I'm not quite sure about VAE and schedulers (do they need to be trained or are they some fixed-steps algorithms?)
3. Probably not too relevant here if the VAE is something need to be trained but off-the-shelf. If they need to be trained, how should we train them? Input and output should be equal dimension and the best result would be VAE just does nothing but produces original input. How do we make it "compress" the input but keep the important info effectively.
4. About text encoders, can we switch it to some other model other than "openai/clip-vit-large-patch14" (say I want to support multi-lingual or a very specific category of text-image pair)? What would be the restrictions here? Or what are the constrains for making the text encoder or even the whole diffusion pipeline more modular. 
5. How does the cross-attention layer work if the UNnet takes 3*64*64 latent but text encoder produces 2*77*768 (I think it's always encoding an empty string for unconditional prompt, thus I guess it's 2*77*768 here) output.
6. If we simply want to denoise a picture, among the 4 parts (text encoder, VAE, UNet, scheduelr) which are still necessary and which don't?