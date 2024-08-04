## https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ/discussions/25

contains_question: yes

question_part: 
1. What are the key differences between GPTQ and NF4 quantisation with bitsandbytes? Are there reasons to expect advantages with one over the other?
2. I notice that there is no quantisation config recommended for inference in the ReadMe
3. Any reason not to use os.environ["SAFETENSORS_FAST_GPU"] = "1" for inference ?
4. Any reason I couldn't use peft and lora to fine tune this model?