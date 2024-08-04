## https://huggingface.co/Thireus/Vicuna13B-v1.1-8bit-128g/discussions/1

contains_question: yes

question_part:
I've been trying to test it using colab since it should fit their GPU (15360 GB VRAM)
But when trying to lauch the server using this command : <pre>python server.py --model Thireus_Vicuna13B-v1.1-8bit-128g --model_type LLaMA --wbits 8 --groupsize 128 --share </pre>
The code returns without any message
<pre> bin /usr/local/lib/python3.9/dist-packages/bitsandbytes/libbitsandbytes_cuda118.so
Loading Thireus_Vicuna13B-v1.1-8bit-128g...
Found the following quantized model: models/Thireus_Vicuna13B-v1.1-8bit-128g/Vicuna13B-v1.1-8bit-128g.safetensors
^C </pre>
I've used both recommended and discouraged method but I have the same issue... Am i doing something wrong