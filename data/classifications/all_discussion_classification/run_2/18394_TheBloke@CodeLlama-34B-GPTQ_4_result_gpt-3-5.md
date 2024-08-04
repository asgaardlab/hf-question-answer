## https://huggingface.co/TheBloke/CodeLlama-34B-GPTQ/discussions/4

contains_question: yes

question_part: I have no clue how to explain this situation:
This model is supposed to be 34B so it should take lots of  VRAM and leave very little memory for context, however in some unknown way it manages to fit 16k tokens into 24gb vram   when even 20B models will only fit 8k
and in fact it can remember what was said in the very beginning of the text if asked the question.