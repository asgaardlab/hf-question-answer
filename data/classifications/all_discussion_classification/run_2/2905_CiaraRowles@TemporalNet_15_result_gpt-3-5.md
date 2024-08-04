## https://huggingface.co/CiaraRowles/TemporalNet/discussions/15

contains_question: yes

question_part: I have a question about your process, since we're writing a demo using the converted Diffusers model on [PR #13](https://huggingface.co/CiaraRowles/TemporalNet/discussions/13) by @patrickvonplaten 

Looking at the configuration on script, could you clarify the steps here? 

1. Initial image + prompt using ControlNet Hed Boundary.
2. Generate Image + prompt,  (no condition) just img2img using TemporalNet
3. LastFrame as init Image + prompt using TemporalNet
4. back to 3 until ends

Are these the steps?