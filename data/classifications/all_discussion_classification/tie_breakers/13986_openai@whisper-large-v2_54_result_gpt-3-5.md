## https://huggingface.co/openai/whisper-large-v2/discussions/54

contains_question: yes

question_part: How to use
```pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v2")```
and set
```model.config.forced_decoder_ids = WhisperProcessor.get_decoder_prompt_ids(language="portuguese", task="transcribe")```