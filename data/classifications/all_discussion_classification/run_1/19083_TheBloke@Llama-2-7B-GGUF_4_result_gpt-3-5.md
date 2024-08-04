## https://huggingface.co/TheBloke/Llama-2-7B-GGUF/discussions/4

contains_question: yes

question_part: GGUF q4_0 model variants quantize the "output.weight" tensor with q6_k (compared to former ggml files which left them at fp32 iirc) Is this intended? It seems to depend on whether `LLAMA_NO_K_QUANTS` is set during compilation and `quantize_output_tensor` during quantization time. Is that something you changed in your process?