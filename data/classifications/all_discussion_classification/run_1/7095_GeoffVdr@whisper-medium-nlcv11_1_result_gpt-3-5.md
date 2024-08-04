## https://huggingface.co/GeoffVdr/whisper-medium-nlcv11/discussions/1

contains_question: yes
question_part: Good day, is it maybe possible to somehow obtain the .pt model, similarly to the format the whisper models are in `~/.cache/whisper/` when doing 'pip install whisper' & running i.e. `model = whisper.load_model('medium')` 
I ask because I'd like to perform batch transcription of longer documents, and running the model through huggingface only allows for up to max_new_tokens =  484 or something like that, requiring all input audio to be split.