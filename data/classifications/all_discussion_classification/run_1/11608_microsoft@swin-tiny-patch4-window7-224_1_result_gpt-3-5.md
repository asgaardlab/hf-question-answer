## https://huggingface.co/microsoft/swin-tiny-patch4-window7-224/discussions/1

contains_question: yes

question_part: 
First,  the input size is torch.size((1, 5, 224, 224)), but the pretrained swin v2 see only support torch.size((3, 224,224)).
Second, I want to extract the feature, in other words,  the output size from swin v2 is torch.size((1,1024,20,20)).
How do I fix the two questions above?