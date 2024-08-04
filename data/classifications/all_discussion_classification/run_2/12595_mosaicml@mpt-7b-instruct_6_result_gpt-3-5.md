## https://huggingface.co/mosaicml/mpt-7b-instruct/discussions/6

contains_question: yes

question_part: Loading the model with the following code (consecutive time):``` generate = InstructionTextGenerationPipeline( "mosaicml/mpt-7b-instruct", torch_dtype=torch.bfloat16, trust_remote_code=True, ) ``` takes way, way more time than loading other, even bigger models (like `databricks/dolly-v2-12b`) on the same hardware.