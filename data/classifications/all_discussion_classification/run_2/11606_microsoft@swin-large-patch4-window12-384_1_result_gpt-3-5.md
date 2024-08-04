## https://huggingface.co/microsoft/swin-large-patch4-window12-384/discussions/1

contains_question: yes

question_part: I have tried to reproduce the accuracy results (models fine tuned on imagenet-1k). The accuracy as reported in the offical github is 87.3 (last row in the attached image). However, this model never reaches to that accuracy. The best accuracy so far is 87.03% (-0.27). This is the command line that I am using for finetuning.  I have found one slight discrepancy between this model and what included in github, that is `DROP_PATH_RATE` which in HF model is 0.1 but in github it is 0.2 (not sure if that makes a huge difference). 

Do you have any suggestions how to get to the reported accuracy?