## https://huggingface.co/LoneStriker/TenyxChat-8x7B-v1-3.5bpw-h6-exl2/discussions/1

contains_question: yes

question_part: There are discussions on our forum about how your quants do not perform too well on long contexts. The stated reason is that you use a default context length of 2048 when quantizing. Looking at the docs in https://github.com/turboderp/exllamav2/blob/master/doc/convert.md, I guess it is a `--length` parameter. Is that the case? Do you have any info about whether this setting has noticeable effect during inference?