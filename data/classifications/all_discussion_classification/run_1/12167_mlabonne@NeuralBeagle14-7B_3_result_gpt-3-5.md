## https://huggingface.co/mlabonne/NeuralBeagle14-7B/discussions/3

contains_question: yes
question_part: 
1. Do models have a harder time learning the concept of "stopping" when they are required to track a sequence of multiple tokens, i.e. `['<', '|', 'im', '_', end', '|', '>']`
2. Does this introduce a problem where certain text sequences can make ambiguous representation of the stop string? I.e. if a model's output ends with `<`, then this tokenizes as `['<<', '|', 'im', '_', end', '|', '>']`, and note how this no longer matches the tokenization of the expected stop sequence, because two `<` in a row get tokenized as `<<` instead of `['<', '<']`. That's just one example, I suppose there could be more. I guess this only has an impact during training, and in rare cases?