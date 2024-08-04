## https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha/discussions/34

contains_question: yes

question_part: 
Why the chosen rewards are negative?
Why both the chosen rewards and rejected rewards are negative, though the reward margins are positive.
The negative chosen rewards essentially indicate that the optimized model does not assign higher probabilities for chosen examples than the reference one, which is not that reasonable.