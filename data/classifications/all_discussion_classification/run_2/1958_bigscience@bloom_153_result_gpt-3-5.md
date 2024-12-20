## https://huggingface.co/bigscience/bloom/discussions/153

contains_question: yes

question_part: 
- Issue 2: Incorrect handling of punctuation in generated text
When a punctuation character (only `!,.?`) is preceded by a space in the prompt, the space is not preserved in the `generated_text` output, even if the prompt was generated by the AI itself. This can be seen in the following example:

```python
>>> inference = InferenceApi("bigscience/bloom", token = HfFolder.get_token())
>>> generated_text = inference("Hello") # Output: "Hello , world"
>>> inference(generated_text) 
'Hello, world and some other text' # Space before "," is not preserved
```