## https://huggingface.co/WizardLM/WizardCoder-15B-V1.0/discussions/10

contains_question: yes  
question_part: We meet an error 'list index out of range' while input question in local model, but it works well both on demo and text-generation webui, which is running the same code. I am very confused about it. I found that the answer will repeat the input question and it will also be counted in the token limits so as to raise error, But why does it work on webui or demo