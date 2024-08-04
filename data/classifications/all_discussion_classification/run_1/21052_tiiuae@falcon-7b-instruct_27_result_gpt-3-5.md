## https://huggingface.co/tiiuae/falcon-7b-instruct/discussions/27

contains_question: yes

question_part: Hi, I'm trying to run this model with the set of padded inputs. I have set the following values:
tokenizer.padding_side = "left"
tokenizer.pad_token_id = 11
Along with the padded set of inputs, I'm not getting the correct results or the same as the non-padded input. Is this expected? Is this model expected to not work with the padded inputs?