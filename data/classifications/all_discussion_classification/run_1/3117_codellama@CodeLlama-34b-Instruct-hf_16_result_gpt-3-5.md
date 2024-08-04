## https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf/discussions/16

contains_question: yes

question_part: I am trying to use HF's inference API to interact with the model from a gradio app. For larger inputs, I receive a validation error: "Input validation error: `inputs` tokens + `max_new_tokens` must be <= 8192". Is this a limitation on this HF implementation or am I using the inference API wrong? From the blog post I read that CodeLlama should support up to 100k tokens in the input. How to achieve that with this model