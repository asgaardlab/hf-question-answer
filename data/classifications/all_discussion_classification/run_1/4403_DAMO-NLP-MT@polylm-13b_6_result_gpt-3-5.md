## https://huggingface.co/DAMO-NLP-MT/polylm-13b/discussions/6

contains_question: yes

question_part: In my experiments, i realize that the model architecture of polylm-13b is difference from polylm-multialpaca-13b version, but in model cards, it was said that multialpaca is a SFT version of polylm-13b. This is so confusing that the model type is not matching that in config of base model polylm the LMhead is PolyLMHead, and in SFT version is GPT2LMHead, can you explain clearly about this mismatching? And if i can using the GPT2LMHead replace for the base model PolyLMHead, and if i can, how can i convert the tensor shape of model to this type of LMHead?