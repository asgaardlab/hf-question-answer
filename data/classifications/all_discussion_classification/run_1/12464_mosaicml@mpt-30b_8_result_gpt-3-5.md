## https://huggingface.co/mosaicml/mpt-30b/discussions/8

contains_question: yes

question_part: I want to finetune the `mpt-30b` and its `instruct` variant on a custom dataset. Is there a reference script / notebook available that shows an example of how to do so? I tried looking around but couldn't find one. I did try to finetune it using a vanilla huggingface `Trainer` with qlora and that didn't seem to work unfortunately. It gave a weird "mpt models do not support gradient checkpointing" error.