## https://huggingface.co/facebook/encodec_48khz/discussions/2

contains_question: yes
question_part: I noticed the model card indicates that this model (the 48kHz stereo EnCodec) was trained on speech, music, and general audio data. However, the paper (https://arxiv.org/pdf/2210.13438.pdf) indicates that the 48kHz stereo model was only trained on music data:
```4.1: Dataset
We train EnCodec on 24 kHz monophonic across diverse domains, namely: speech, noisy speech, music and
general audio while we train the fullband stereo EnCodec on only 48 kHz music.
```
It appears the model cards are almost identical between the 24kHz mono and 48kHz stereo models - perhaps this difference can be documented here for the 48kHz checkpoint, to reduce potential confusion.