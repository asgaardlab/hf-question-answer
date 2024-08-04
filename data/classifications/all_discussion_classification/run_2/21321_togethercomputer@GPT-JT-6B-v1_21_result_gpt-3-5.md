## https://huggingface.co/togethercomputer/GPT-JT-6B-v1/discussions/21

contains_question: yes

question_part: 
- How was the mixture sampled and packed for sequence length 2048?
- Specifically, does a single 2048-length sequence consist of packed examples from a single dataset, unpacked examples from a single dataset, or packed examples individually sampled from the overall mixture?
- How were NI/P3 examples deduplicated? The original dataset cards mention there are potential duplicate inputs
- Were the instruction datasets (CoT, NI, P3) trained with zero-shot or few-shot prompts?
- a few shot prompt would include an example in the prefix portion of the input, which seems particularly salient for CoT.