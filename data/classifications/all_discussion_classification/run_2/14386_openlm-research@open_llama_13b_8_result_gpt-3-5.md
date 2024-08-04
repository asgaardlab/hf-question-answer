## https://huggingface.co/openlm-research/open_llama_13b/discussions/8

contains_question: yes
question_part: I am trying to load the model using the deepspeed library. Is it possible to optimize this model using this library? I have tried setting 

```python
replace_with_kernel_inject=True
```
But it duplicated the amount of GPU Ram needed. Is there any solution