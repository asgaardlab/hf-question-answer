## https://huggingface.co/t5-small/discussions/4

contains_question: yes

question_part: Is there a way to obtain the output generation logits for greedy decoding, something like "model.generate(input_ids).logits"? However, I think this might output incorrect probabilities owing to the teacher forcing. Is that correct?