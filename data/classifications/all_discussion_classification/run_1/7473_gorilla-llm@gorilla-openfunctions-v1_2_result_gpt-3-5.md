## https://huggingface.co/gorilla-llm/gorilla-openfunctions-v1/discussions/2

contains_question: yes  
question_part: 
1) this does not seem to work
```python
openai.api_key = "EMPTY"
openai.api_base = "http://luigi.millennium.berkeley.edu:8000/v1"
completion = openai.ChatCompletion.create(model="gorilla-openfunctions-v1", ...)
```
while it works for `gorilla-openfunctions-v0` model

2) maybe in the future I will create an HF space based on your model