## https://huggingface.co/openai/whisper-large-v3/discussions/42

contains_question: yes

question_part: 
1. Why this model is not working with the dtype as given in config.json? If I explicitly define dtype for Large-V3 model, what other changes I should make for it to work?
2. I also tried with all other Whisper models (tiny, base, small, and medium, all of which have dtype as float32 in config.json). I also faced this problem of using (torch_dtype=torch.float16) there. For this case, is it even possible to use (any) Whisper pytorch model with different dtype than for the entry in config.json or I'm making any basic mistake? If it is possible to use with different dtype, what adaptation I need to make?