## https://huggingface.co/glaiveai/glaive-function-calling-v1/discussions/1

contains_question: yes

question_part: When attempting to execute this code in Colab, I encountered the following error: "You are using config.init_device='cpu', but you can also use config.init_device="meta" with Composer + FSDP for fast initialization." Subsequently, the CPU resources became fully utilized, leading to a session crash.