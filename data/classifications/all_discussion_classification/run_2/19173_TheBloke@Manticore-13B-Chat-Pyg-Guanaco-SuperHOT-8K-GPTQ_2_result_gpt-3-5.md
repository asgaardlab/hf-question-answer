## https://huggingface.co/TheBloke/Manticore-13B-Chat-Pyg-Guanaco-SuperHOT-8K-GPTQ/discussions/2

contains_question: yes

question_part: ExllamaHF runs fast (relatively), i use it with mythomax model, but after a few text gens the responses are now gibberish. So can someone recommend a setup for running this model in oobabooga please? Until i buy new...i have a 8gb gpu unfortunately. I want to utilize the 8k context so its currently set to: max_seq_len 8192, alpha_value 1, rope_freq_base 0, compress_pos_emb 1. I set comp pos emb to 2 and it fixed the responses but also negates having the larger 8k context, does it not? and wouldnt setting it to 4 make the context 2k effectively?