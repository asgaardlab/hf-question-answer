## https://huggingface.co/speechbrain/asr-wav2vec2-commonvoice-fr/discussions/1

contains_question: yes

question_part: Concerning the checkpoints available through the google drive (README file of the asr-wav2vec2-ctc-fr recipe), is there any change that should be done on the scripts? I've found two issues when running the pre-trained model:
- Locally: large WER (73.46) when running the train script on inference mode (asr_brain.fit section commented in the main)
- Remotely: recurrent error of "forward() expects 2 arguments but 3 were given](TypeError: forward() takes 2 positional arguments but 3 were given". This error was never seen when running the script locally. I believe it may be due to the singularity used. Is there any speechbrain/pytorch singularity readily available?