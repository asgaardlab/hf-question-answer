## https://huggingface.co/bigcode/starcoder/discussions/78

contains_question: yes

question_part: How to save and load the Peft/LoRA Finetune
I am trying to further finetune `Starchat-Beta`, save my progress, load my progress, and continue training. But whatever I do, it doesn't come together. Whenever I load my progress and continue training, my loss starts back from _zero_ (3.xxx in my case).
I'll run you through my code and then the problem.