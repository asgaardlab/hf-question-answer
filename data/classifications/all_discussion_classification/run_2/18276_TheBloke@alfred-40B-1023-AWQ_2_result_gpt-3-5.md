## https://huggingface.co/TheBloke/alfred-40B-1023-AWQ/discussions/2

contains_question: yes
question_part:
Hello,
When running the model with a Transformers pipeline, I see the following warning:
```
/xx/.pyenv/versions/3.10.4/lib/python3.10/site-packages/transformers/generation/utils.py:1473: UserWarning: You have modified the pretrained model configuration to control generation. This is a deprecated strategy to control generation and will be removed soon, in a future version. Please use and modify the model generation configuration (see https://huggingface.co/docs/transformers/generation_strategies#default-text-generation-configuration )
```
Does anyone manage to avoid this?
Does it comes from a model configration change done in the AWQ version or in the unquantized alfred-40b-1023 version?
Thanks