## https://huggingface.co/huggingface/time-series-transformer-tourism-monthly/discussions/2

contains_question: yes

question_part: If you have the time to answer, I would like to ask a question about dimensionality of the inputs. I see that the model always expects the past_input's shape to be (batch_size, context_length+max(lags_sequence)). Does this mean that I have to provide #context_length additional lag steps in my inputs?