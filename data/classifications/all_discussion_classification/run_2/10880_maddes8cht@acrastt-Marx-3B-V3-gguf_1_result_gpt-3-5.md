## https://huggingface.co/maddes8cht/acrastt-Marx-3B-V3-gguf/discussions/1

contains_question: yes

question_part: I often get error from `ctransformers` when importing some GGUF models. Here is the code example
```python
from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("maddes8cht/acrastt-Marx-3B-V3-gguf", model_file="maddes8cht/acrastt-Marx-3B-V3-gguf", model_type='stablelm')
print(llm("AI is going to"))
```
It actually downloaded the `.gguf` file from repo, but returned this error message
```python
RuntimeError: Failed to create LLM 'stablelm' from '/root/.cache/huggingface/hub/models--
```