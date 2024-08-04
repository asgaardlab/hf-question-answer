## https://huggingface.co/declare-lab/flan-alpaca-xl/discussions/5

contains_question: yes
question_part: Why does my CPU outperform my GTX 3060 Mobile GPU when running declare-lab/flan-alpaca-xl locally
I've noticed something unusual when running the model: The performance is much faster when the model runs solely on the CPU as opposed to using the GPU. This is despite setting the device_map to "auto", which should theoretically take advantage of both CPU and GPU resources.