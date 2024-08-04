## https://huggingface.co/RuterNorway/Llama-2-13b-chat-norwegian-GPTQ/discussions/2

contains_question: yes

question_part: Since 🤗transformers now has native support for GPTQ-quantized models, quantized models can now be loaded and used just by calling `AutoModelForCausalLM.from_pretrained('your_model')` TheBloke GPTQ models already support this but yours doesn't yet. It would be nice to see this change, as it then could be directly used in many scripts without much code alteration. I have already done this on a private repo, so I'll let you know the steps I took to make it work: 1. Rename the safetensors model file to model.safetensors 2. The safetensors file lacks metadata, which the 🤗transformers backend relies on. Therefore, add metadata.