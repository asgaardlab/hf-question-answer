## https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0/discussions/9

contains_question: yes

question_part: I have tried these models with better current scores then upstage/SOLAR-10.7B-Instruct-v1.0:
- rwitz2/go-bruins-v2.1.1
- ignos/LeoScorpius-GreenNode-Alpaca-7B-v1
- Toten5/LeoScorpius-GreenNode-7B-v1

and found that all of them hallucinate more often than the SOLAR does. 

Probably, the reason is:
a) in the size of the model and it is more perspective to improve 11B models than 7B. 
b) they are overtrained on the test dataset data.