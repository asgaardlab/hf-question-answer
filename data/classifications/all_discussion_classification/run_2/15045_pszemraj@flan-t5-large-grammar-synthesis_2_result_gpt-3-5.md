## https://huggingface.co/pszemraj/flan-t5-large-grammar-synthesis/discussions/2

contains_question: yes

question_part: Hello, I wasn't sure if this change would also affect your model since it also uses T5-Large, but I happened to see something about the "gelu" function in the config.json needing to be changed from ( "feed_forward_proj": "gelu",) to ( "feed_forward_proj": "gated-gelu", ) and wanted to pass it along incase it's something of interest to you.