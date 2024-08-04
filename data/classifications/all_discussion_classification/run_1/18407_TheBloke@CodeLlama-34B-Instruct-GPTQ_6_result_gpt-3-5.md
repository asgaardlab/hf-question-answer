## https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GPTQ/discussions/6

contains_question: yes  
question_part: Looks like a change in [this file](https://github.com/huggingface/text-generation-inference/blob/0a63e9ab688cf715d31574ee5bb31025ff22ceec/server/text_generation_server/models/custom_modeling/flash_llama_modeling.py#L4) will fix the issue according to [this comment](https://github.com/huggingface/text-generation-inference/issues/769#issuecomment-1664596806), but I am not sure what exactly would need to be done. If someone can point me in the right direction I can raise a PR. 

Also number of shards seems to make a difference in some cases. Is that expected to be the case here?