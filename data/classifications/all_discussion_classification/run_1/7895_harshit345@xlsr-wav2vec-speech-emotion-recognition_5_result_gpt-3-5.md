## https://huggingface.co/harshit345/xlsr-wav2vec-speech-emotion-recognition/discussions/5

contains_question: yes
question_part: Hey, I'm trying to run this model with the provided sample Code. But I haven't found any information about the Wav2Vec2ForSpeechClassification Class. I think the Huggingface Hub hasn't provided such a Class. Even ehcalabres, who made another emotion speech recognition Model, made a Request to add such a Class to the Transformers Library. I worked around this problem using the Wav2Vec2ForSequenceClassification Class, but the results in Emotions are always pretty similar (Anger: 17.3% | Disgust: 15.1% | Fear: 23.3% | Happiness: 23.7% | Sadness: 20.7%). It doesnt matter what audio file I use, its always similar to that, so maybe I'm using the wrong class. Can anyone provide me with Information of where this Class is located, how to use it or has the Code of Wav2Vec2ForSpeechClassification?