## https://huggingface.co/microsoft/git-large-coco/discussions/1

contains_question: yes

question_part:  I've also tried to fine-tune the model using the code in this tutorial: https://colab.research.google.com/drive/1HLxgrG7xZJ9FvXckNG61J72FkyrbqKAA. That seemed to work, but when I tried to save a checkpoint every epoch, those checkpoints produced strange output on my test set (the model gave the same output for each input image), and the output of the last checkpoint was different to that of the final model that was in memory after conclusion of the training loop (that one actually produced different output for different images), so something seemed to go wrong there. 

I used the same code as in thet tutorial, it was only different here: