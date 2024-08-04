## https://huggingface.co/Guernika/CoreMLStableDiffusion/discussions/10

contains_question: yes

question_part: The download does not start at all (loading wheel) then a few minutes later this message pops :
![IMG_9503838F89C2-1.jpeg](https://cdn-uploads.huggingface.co/production/uploads/1677230047283-631b0ae0f6bc4be4a64b33f8.jpeg)  
I can't figure out the direct download method from url, I linked the chunked.zip without success

Also, I'm trying to convert custom inpainting but I got this error:
size mismatch for conv_in.weight: copying a param with shape torch.Size([320, 9, 3, 3]) from checkpoint, the shape in current model is torch.Size([320, 4, 3, 3]).
Searching the internet lead to nothing related (some naming stuff), so I gave it a shot on sd-v1-5-inpainting and got the same error.
Since we got a working inpainting model I guess there is some sprinkle of magic to add in the recipe?