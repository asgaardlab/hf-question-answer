## https://huggingface.co/speechbrain/mtl-mimic-voicebank/discussions/4

contains_question: yes

question_part: I've managed to fine-tune the ASR model, the last step in this recipe, however I'm struggling to understand how I can easily use an inference class to transcribe enhanced audio files with the model. It seems like the pretrained ASR model may use a encoder decoder interface, but the modules produced in the hyperparameters final output are different from what is expected by that interface. Clearly based on the 'test_stats' a model is produced that can perform ASR, but what interface to use for inference is a bit unclear - whether this needs to be something custom, or if it's simpler than that. If you could provide some clarity regarding this, that would be helpful.