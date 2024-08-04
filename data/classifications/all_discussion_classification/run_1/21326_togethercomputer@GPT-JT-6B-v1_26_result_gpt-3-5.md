## https://huggingface.co/togethercomputer/GPT-JT-6B-v1/discussions/26

contains_question: yes

question_part: Hello, I've been trying to replicate the GPT-JT spaces demo results locally. So far the results are getting close to the demo but seems to be struggling for tasks that require deeper contextual understanding like answering questions from give examples. I've noticed by changing the "stop, split by" parameter on the web demo from the default, the model also seems to struggle on tasks it previously was performing well at. However, there doesn't seem to be an argument that is settable in the Transformers pipeline. Could anyone provide an explanation on how or if setting "stop, split by" is possible locally?