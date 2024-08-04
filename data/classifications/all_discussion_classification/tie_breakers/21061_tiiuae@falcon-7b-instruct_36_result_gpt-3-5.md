## https://huggingface.co/tiiuae/falcon-7b-instruct/discussions/36

contains_question: yes

question_part: While I manage to load the model it then maxes out the memory when I try to generate samples. Digging a bit into this while doing some profiling on a different machine I found that the amount of RAM is used on model.generate() function is 2x model size, something I am not experiencing with other models. The amount of additional resources requested seems like a copy of the model is loaded onto the same device. Anyone experience anything similar?