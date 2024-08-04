## https://huggingface.co/tiiuae/falcon-40b/discussions/3

contains_question: yes
question_part: [Bug] Does not work

Used example script with latest pytorch, einops, and transformers but it does not work:

Traceback (most recent call last):
  File "/home/catid/sources/supercharger/test_falcon_basic.py", line 8, in <module>
    pipeline = transformers.pipeline(
  File "/home/catid/mambaforge/envs/supercharger/lib/python3.10/site-packages/transformers/pipelines/__init__.py", line 788, in pipeline
    framework, model = infer_framework_load_model(
  File "/home/catid/mambaforge/envs/supercharger/lib/python3.10/site-packages/transformers/pipelines/base.py", line 278, in infer_framework_load_model
    raise ValueError(f"Could not load model {model} with any of the following classes: {class_tuple}.")
ValueError: Could not load model tiiuae/falcon-40b with any of the following classes: (<class 'transformers.models.auto.modeling_auto.AutoModelForCausalLM'>,).