## https://huggingface.co/TheBloke/Llama-2-7B-32K-Instruct-GGUF/discussions/1

contains_question: yes  
question_part: However, in my experience, I had to still explicitly [add `--rope-freq-scale 0.125`](https://github.com/ggerganov/llama.cpp/issues/2530#issuecomment-1667946460) to get sensible output, even after passing `-c 32768` as an argument. Without that, I was only getting spaces and new-lines in the output (probably token 0?)