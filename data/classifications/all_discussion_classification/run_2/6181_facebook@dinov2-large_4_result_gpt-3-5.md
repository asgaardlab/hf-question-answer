## https://huggingface.co/facebook/dinov2-large/discussions/4

contains_question: yes
question_part: I was wondering why the image size in the config model (  "image_size": 518) is :
518
while in the image processor images are resized to 256 and then cropped to 224.
In my understanding, they should be the same to get better performances, isn't it?
Moreover, I didn't fully understand the utility of rescaling in the image processor with the following factor :
  "rescale_factor": 0.00392156862745098
Is this done in the original model implementation ?