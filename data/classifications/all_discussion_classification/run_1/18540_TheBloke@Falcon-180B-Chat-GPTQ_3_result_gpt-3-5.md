## https://huggingface.co/TheBloke/Falcon-180B-Chat-GPTQ/discussions/3

contains_question: yes

question_part: Hi, just want to provide a little feedback. I was able to run the 3bit version on a single A100 80GB and the quality from my short tests looks incredibly close to the full 16bit version (tried on the HF space), the model’s quality looks very close to Llama-2-70B though (as anticipated by the leaderboard). Inference speed looks a bit poor (I obtain 8 token/sec while with llama-70-gptq i get from 80 to 160 token/sec) but I belive it’s normal.