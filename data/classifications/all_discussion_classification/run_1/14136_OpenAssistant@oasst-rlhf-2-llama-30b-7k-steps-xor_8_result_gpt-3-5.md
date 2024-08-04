## https://huggingface.co/OpenAssistant/oasst-rlhf-2-llama-30b-7k-steps-xor/discussions/8

contains_question: yes  
question_part: Only difference is I'm using device_map auto to make use of both GPUs. (Also happens for `.to('cuda')`,  `.to(0)`, `.to(1)` instead of `.to(model.device)`.)