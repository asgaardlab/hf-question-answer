## https://huggingface.co/bigscience/bloomz/discussions/45

contains_question: yes

question_part: Why is version 176b of the model in bfloat16 while the other models (3b, 7b) are in float16? Does anyone know the reason for such a choice? Similarly, is the bfloat16 type relevant because it appears to maintain the same dynamic range as float32 but at the expense of precision? In general, the values involved are small, so float16, which has better precision, seems more appropriate, right?