## https://huggingface.co/TheBloke/guanaco-33B-GPTQ/discussions/11

contains_question: yes  
question_part: Does anyone have suggestions on what further optimizations might be possible?  text-generation-webui uses CUDA 11.7, which I understand does not take full advantage of the Ada Lovelace architecture, so I'd be curious what kind of speedup might be possible with CUDA 11.8 or even 12.1 (which I understand works with the latest Pytorch builds).