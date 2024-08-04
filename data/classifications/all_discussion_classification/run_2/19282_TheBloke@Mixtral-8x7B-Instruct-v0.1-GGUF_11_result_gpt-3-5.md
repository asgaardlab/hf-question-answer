## https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/discussions/11

contains_question: yes  
question_part: @TheBloke just wanted to bring your attention to [this](https://github.com/ggerganov/llama.cpp/pull/4406#issuecomment-1855151885) GitHub comment in case you have not seen in yet. It strongly suggest that there is something seriously wrong with the Q6_K quant as it has far higher perplexity than even Q4_0 when using 2 experts. The test does not include Q4_K_M or Q5_K_M, I think it would be a good idea to run a perplexity test on those two as well to make sure this issue does not affects all of the K variants.