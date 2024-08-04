## https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-4bit_g64-HQQ/discussions/3

contains_question: yes

question_part: Serving with TGI or vLLM?
Can the models be served with either of these containers - I did not see any HQQ support in either.
What CUDA level is necessary? AWQ for example on vLLM is currently only available on Ampere onwards (CUDA compute level 7.5+).
Being able to serve Mixtral models from a single V100 32GB (CUDA 7.0) would be a big plus to use those older GPUs, too.