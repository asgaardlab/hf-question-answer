## https://huggingface.co/cerebras/btlm-3b-8k-base/discussions/16

contains_question: yes

question_part: How to reproduce quantized memory usage?
I see that you have figures below 4gb. How do I reproduce that?  When I use BitsAndBytesConfig(load_in_4bit=True), I get memory usage of 4.3gigs of VRAM on cuda.