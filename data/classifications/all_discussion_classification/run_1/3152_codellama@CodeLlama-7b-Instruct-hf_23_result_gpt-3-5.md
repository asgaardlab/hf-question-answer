## https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf/discussions/23

contains_question: yes  
question_part: 
Hello everyone, I would like to know if someone could help me with this or provide some suggestions on what to do. What I want is to use the theoretical 100K input for the codellama-instruct input prompt. I am using 8 GPUs with 32GB each, but when I try to send a very long input prompt, I get this message. It's as if it's only using 1 GPU to process the input and ignoring the others. This issue doesn't occur when generating a long output since all the GPUs work correctly. It only happens when I send a very long input prompt. I would appreciate any help or suggestions you may have.