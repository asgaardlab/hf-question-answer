## https://huggingface.co/facebook/musicgen-large/discussions/16

contains_question: yes

question_part: However, when changing the text condition in step 4, ex: text condition is `"80s pop track with bassy drums and synth", "90s rock song with loud guitars and heavy drums"`, a runtime error will be thrown: 

I expected this would work without issue since the model should treat each iteration from step 3 as a separate prompt processing, or am I misunderstanding something in here?