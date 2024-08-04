## https://huggingface.co/TheBloke/CodeLlama-34B-GGUF/discussions/3

contains_question: yes

question_part: Hi, I am trying to quantize a model, and I see you have achieved it. So, could you share the process? I downloaded the model and llama.cpp. Then I move the model to the model's folder of llama.cpp and run convert.py file. So I get the gguf file. But then I run !python /llama.cpp/examples/quantize models/[model-folder]/[model]-f32.gguf /models/llama2-bg/[model]-q4_0.bin q4_0 and I get error: /usr/bin/python3: can't find '__main__' module in '/content/llama.cpp/examples/quantize'. I would highly appreciate it if you could help me with this.