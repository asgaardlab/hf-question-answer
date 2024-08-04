## https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/discussions/6

contains_question: yes
question_part: My suspicion is that the problem lies in how the source images were prepared before training.  That is to say, if the training data's portrait aspect-ratio images were coerced into a square aspect ratio via simple center-cropping, then this is precisely the output I'd expect to see from the model.