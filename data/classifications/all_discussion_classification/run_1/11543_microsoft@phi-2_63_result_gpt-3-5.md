## https://huggingface.co/microsoft/phi-2/discussions/63

contains_question: yes

question_part: I was wondering what could be the reason, it it `max_new_token` parameter? Do we need to set it up explicitly for every query, after guessing what could be the length where Phi-2 won't add some redundant texts.

Second question I have is regrading support of sampling of generated text. I noticed below statement in model-card section, does this mean that along with beam search, Top-k or Top-p samplings are irrelevant to Phi-2 somehow and it is best while greedy decoding only? 

I tried multiple flavour code-generation, Chat-mode, Instruction-output, Sampling method gave worst results. Are there any specific reasons or I am doing something wrong with sampling or any other parameter passing?