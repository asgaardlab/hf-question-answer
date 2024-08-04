## https://huggingface.co/bigcode/starcoder/discussions/87

contains_question: yes

question_part: Challenge: I am able to iterate thru all files and get recommendations independently. But when running in a single flow in a loop, after the first file is encoded and decoded, for the second file, the input_ids of the previous file remains. How to remove the input_ids tokens of the previous file.