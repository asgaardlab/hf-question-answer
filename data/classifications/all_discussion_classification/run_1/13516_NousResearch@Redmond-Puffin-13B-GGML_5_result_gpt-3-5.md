## https://huggingface.co/NousResearch/Redmond-Puffin-13B-GGML/discussions/5

contains_question: yes
question_part: From what I understand, Llama2 was trained with a specific conversation "flow" format, utilising SYS/ INS tags, etc.
Does this mean, this particular model overrides the training of base llama2 model, and those SYS etc tags are not required ?
Or does this mean, both "templates" will work, and llama2 template will "trigger" responses coming from the base model, and suggested here "### human:" etc prompts will trigger responses utilising what this particular model adds on top of base llama2 model ?
Is it possible/necessary to use both of those prompt formats at the same time/interchangeably ?