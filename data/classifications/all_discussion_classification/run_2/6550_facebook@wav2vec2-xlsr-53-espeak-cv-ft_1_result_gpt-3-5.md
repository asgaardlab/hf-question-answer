## https://huggingface.co/facebook/wav2vec2-xlsr-53-espeak-cv-ft/discussions/1

contains_question: yes

question_part: 
"When running the demo, I get the following
"Can't load tokenizer using from_pretrained, please update its configuration: Wav2Vec2PhonemeCTCTokenizer requires the phonemizer library but it was not found in your environment. You can install it with pip: `pip install phonemizer`"
This also happens if I try to load the model using the pipeline function from a Terminal. After installing phonemizer and espeak, I get another message: "RuntimeError: espeak not installed on your system""