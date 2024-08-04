## https://huggingface.co/bigscience/bloom/discussions/150

contains_question: yes
question_part: 
- **First:** when I switch the model to greedy in the huggingface API, it works fine, but when I set `"do_sample": False` in my request, it returns different results each time. Is there any possibility to force Bloom to be more deterministic?
- **Second:**  when i get response in json it skips space before punctuation e. g. "bla , bla" -> "bla, bla". Is there a way to avoid this behavior?