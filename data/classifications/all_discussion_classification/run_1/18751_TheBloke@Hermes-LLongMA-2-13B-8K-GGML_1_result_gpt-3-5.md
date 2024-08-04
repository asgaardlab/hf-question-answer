## https://huggingface.co/TheBloke/Hermes-LLongMA-2-13B-8K-GGML/discussions/1

contains_question: yes

question_part: On the Model card, under "How to run in llama.cpp", the example command line limits the context to 2048 instead of the 8192 this model supports:
What would the proper command be? Besides raising the context size, does it require scaling parameters like `--rope-freq-base` or `--rope-freq-scale`