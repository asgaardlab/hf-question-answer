## https://huggingface.co/hkunlp/instructor-xl/discussions/14

contains_question: yes

question_part: I'm not sure why the GPU memory requirements suddenly increase. I suspect that it might be due to data longer than the model's max_length (which is set to the default value of 512) getting truncated into multiple entries, resulting in individual batch sizes larger than 128 and leading to OOM errors. Later, I strictly limited the input data to a length of 512 tokens, but still encountered the same OOM errors. I have no more idea about the possible reasons.