## https://huggingface.co/TheBloke/mpt-30B-chat-GGML/discussions/7

contains_question: yes

question_part: I'm curious how/why the base length is 8,000. Was max_seq_len just set like this as config (since the model uses ALiBi).
I assume I could set max_seq_len to a higher value, or is that configuration hard coded for a given quantized model?
Lastly, is the main benefit of quantization that you get some reduction in the model size and run time (say a reduction to 5/16ths of size if using int5 versus fp16 (or is it bf16)?