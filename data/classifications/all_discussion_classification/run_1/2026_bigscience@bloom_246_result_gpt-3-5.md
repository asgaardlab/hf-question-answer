## https://huggingface.co/bigscience/bloom/discussions/246

contains_question: yes

question_part: 
1. Continued pretraining. To our knowledge, this seems to be the easiest way forward. We currently anticipate running the training with all weights unfrozen, for 1 epoch and 256 as effective batch size. What could you recommend using as hyperparameters? In particular:
1.1 Would you recommend freezing a certain set of weights? 
1.2 Which learning rate (paradigm) would you propose? 
1.3 How would these decisions scale across different model sizes?

2. Alternatively, we would think to use MAD-X adapters just as Yong et al (https://arxiv.org/pdf/2204.04873.pdf).
2.1 Would you recommend this approach over continued pretraining? And if so, where in what capacity would you recommend plugging in the adapters (again in function of the BLOOM model size)?