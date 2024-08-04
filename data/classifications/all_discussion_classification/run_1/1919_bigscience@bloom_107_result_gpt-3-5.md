## https://huggingface.co/bigscience/bloom/discussions/107

contains_question: yes

question_part: I want to know why the [hosted inference API](https://huggingface.co/bigscience/bloom) for BLOOM with the interactive playground on HuggingFace is so fast. On my hardware and just like many other people reported in the inference benchmarks, the inference speed is slow with HuggingFace `accelerate`. The throughput on 8x A100 with the HuggingFace framework in this [link](https://github.com/bigscience-workshop/Megatron-DeepSpeed/tree/main/scripts/bloom-inference-scripts) is about four tokens per second under batch size 1 (230ms per token). But I feel like the HuggingFace interactive playground is way faster than this. 

Any tips for doing the inference faster as the Huggingface hosted API? Is the hosted inference API a quantized version of BLOOM (for example, the int8 version) or the runtime is powered by a different framework such as Microsoft `DeepSpeed`?