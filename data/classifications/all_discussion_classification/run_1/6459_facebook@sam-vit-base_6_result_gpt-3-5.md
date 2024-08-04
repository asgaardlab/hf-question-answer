## https://huggingface.co/facebook/sam-vit-base/discussions/6

contains_question: yes

question_part: I used this :
https://github.com/huggingface/transformers/tree/main/src/transformers/models/sam
there are 4 prompts available boxes, labels, masks, and points. Can I use only one of prompt? If I specify boxes, it can run smoothly. When I use masks only it gives me error AssertionError: ground truth has different shape (torch.Size([14, 1, 256, 256])) from input (torch.Size([1, 1, 256, 256])) when calculating loss because the model gives 1 channel instead of 14 (num of segmented objects). Similar happened when I used labels only but when combined with points it gives me error RuntimeError: Sizes of tensors must match except in dimension 2. Expected size 1 but got size 14 for tensor number 1 in the list. Running use points only run smoothly.