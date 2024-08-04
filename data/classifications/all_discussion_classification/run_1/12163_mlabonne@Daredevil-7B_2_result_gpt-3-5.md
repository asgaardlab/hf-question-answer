## https://huggingface.co/mlabonne/Daredevil-7B/discussions/2

contains_question: yes
question_part: I'd like to ask you a question. In the yaml file:
```yaml
models:
  - model: mistralai/Mistral-7B-v0.1
    # No parameters necessary for base model
  - model: samir-fama/SamirGPT-v1
    parameters:
      density: 0.53
      weight: 0.4
  - model: abacusai/Slerp-CM-mist-dpo
    parameters:
      density: 0.53
      weight: 0.3
  - model: EmbeddedLLM/Mistral-7B-Merge-14-v0.2
    parameters:
      density: 0.53
      weight: 0.3
merge_method: dare_ties
base_model: mistralai/Mistral-7B-v0.1
parameters:
  int8_mask: true
dtype: bfloat16
```