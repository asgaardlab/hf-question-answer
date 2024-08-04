## https://huggingface.co/mrm8488/falcoder-7b/discussions/2

contains_question: yes

question_part: 
I am having some trouble figuring out how EOS is supposed to work here, neither token_id=2 nor token_id=11 seem to work.  When I try to use the GenerationConfig class to load the `generation_config.json` from this model as per the model card it complains that `pad_token_id` isn't set.