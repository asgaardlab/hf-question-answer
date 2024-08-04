## https://huggingface.co/google/switch-large-128/discussions/6

contains_question: yes

question_part: When I executed the example code in the model card with 4 GPUs, it worked well.

But when I tried it with 3 or fewer GPUs, for example CUDA_VISIBLE_DEVICES=0,1 , it doesn't work and showed the following error.

It came from here.

`RuntimeError: expected scalar type Float but found BFloat16`