## https://huggingface.co/TheBloke/tulu-30B-GPTQ/discussions/2

contains_question: yes
question_part: I saw your note about the prompt, and dug into it a little. What might not be clear (I'll fix this in our readmes shortly) is that we use an additional newline after `<|assistant|>`. I played around with your model briefly and this seemed to make a big difference, and might explain what you saw when using our model: