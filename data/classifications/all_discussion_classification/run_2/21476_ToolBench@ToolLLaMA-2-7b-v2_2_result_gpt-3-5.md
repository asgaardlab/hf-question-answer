## https://huggingface.co/ToolBench/ToolLLaMA-2-7b-v2/discussions/2

contains_question: yes

question_part: Unfortunately, when I run the code I get the following error (which seems not to be my fault):
```
Traceback (most recent call last):
  File "/home/eve/Documents/llm-agent-poc/scripts/download_model_hf.py", line 24, in <module>
    test = pipeline(model=model, tokenizer=tokenizer)
  File "/home/eve/Documents/llm-agent-poc/.venv/lib/python3.10/site-packages/transformers/pipelines/__init__.py", line 801, in pipeline
    raise RuntimeError(
RuntimeError: Inferring the task automatically requires to check the hub with a model_id defined as a `str`. LlamaForCausalLM(