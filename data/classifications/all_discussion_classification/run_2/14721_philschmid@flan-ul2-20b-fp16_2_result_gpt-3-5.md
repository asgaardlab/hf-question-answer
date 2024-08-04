## https://huggingface.co/philschmid/flan-ul2-20b-fp16/discussions/2

contains_question: yes

question_part: I get the following error when I try to deploy this to an endpoint with 4xT4s:
'''RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:2 and cuda:1! (when checking argument for argument index in method wrapper__index_select)'''
Do you have any tips by any chance @philschmid ?