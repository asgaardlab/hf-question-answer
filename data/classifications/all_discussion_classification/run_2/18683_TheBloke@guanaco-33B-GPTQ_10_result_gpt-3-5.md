## https://huggingface.co/TheBloke/guanaco-33B-GPTQ/discussions/10

contains_question: yes

question_part: 
How to finetune the model

How can I finetune the model further? Inference works without problems.
I can do finetuning with the LoracConfig set to
```python
config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["lm_head"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
```
but trying any other target_modules (or removing that line) leads to the error

RuntimeError: self and mat2 must have the same dtype