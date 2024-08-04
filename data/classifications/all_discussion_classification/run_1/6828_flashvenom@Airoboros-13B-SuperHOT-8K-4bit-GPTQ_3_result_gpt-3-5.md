## https://huggingface.co/flashvenom/Airoboros-13B-SuperHOT-8K-4bit-GPTQ/discussions/3

contains_question: yes

question_part: Originally the model card said for ExLlama that you had to manually add the patch which I couldn't figure out how to do, then you recently updated it with this note:
If you are using exllama the monkey-patch is built into the engine, please use -cpe to set the scaling factor, ie. if you are running it at 4k context, pass -cpe 2 -l 4096
This may work from running on a command-line but does not specify how to pass those parameters to Oobabooga. Applying them to the CMD_FLAGS after `--loader exllama` or `--monkey-patch` is not a recognized argument. Also, that example doesn't indicate whether cpe goes up to 4 for 8k context or down to 1, requiring further pre-requisite knowledge to use this model properly