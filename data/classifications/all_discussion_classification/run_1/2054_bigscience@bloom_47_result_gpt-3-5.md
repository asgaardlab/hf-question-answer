## https://huggingface.co/bigscience/bloom/discussions/47

contains_question: yes

question_part: 
2) What is our definition for a training language? The training data has 341B tokens, so at 0.00002%, there are ~68200 tokens of Chi Tumbuka in there.  In English 1 token ~ 0.75 words (a)) and 1 sentence ~ 20 words (b)). If it's ~the same in Chi Tumbuka, the model has seen 2500 sentences of that language, as we did ~1 epoch. Do we have statistics for how much German or Japanese accidentally landed in the training data? I'd guess it's more than Chi Tumbuka, so where do we draw the line between a "training language"? We don't have any evaluation datasets for Chi Tumbuka afaik, so if we don't get on one of its 3M speakers we'll never know if it knows it at all. 👻