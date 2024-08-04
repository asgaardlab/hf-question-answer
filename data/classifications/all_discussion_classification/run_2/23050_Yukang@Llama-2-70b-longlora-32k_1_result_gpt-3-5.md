## https://huggingface.co/Yukang/Llama-2-70b-longlora-32k/discussions/1

contains_question: yes
question_part: From the paper, it appears you managed to achieve an effective batch size of 64 on 8xA100, described as gradient accumulation = 8 x batch size = 8. Was that statement in the paper only for the smaller models, or did it apply to the 70B model @ 32K context as well?  It also looks like you used LORA (as opposed to QLORA or GPTQ-LORA), and it doesn't seem like you used bitsandbytes (load_in_8_bit), so I'm curious what batch size you achieved with 8xA100 using your method.