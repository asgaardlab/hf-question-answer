## https://huggingface.co/TheBloke/LongChat-13B-GPTQ/discussions/1

contains_question: yes

question_part: 
Does max_position_embeddings really the parameter to be changed?
When I'm looking at the `config.json` from longchat, the value of `max_position_embeddings` still 2048, but the `max_sequence_length` is set to 16384. I don't understand what is the difference? And why your `config.json` did not contain `max_sequence_length`