## https://huggingface.co/haor/Evt_V2/discussions/2

contains_question: yes

question_part: The issue comes in the decoding, where utf-8 decoding throws the error "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte". I assume this is due in some way to the VAE encode/decode cycle, but I'm not sure what to do about it. Trying to force a string with str() also gives it a decode error. If you could tell me what I can do to fix this, please do.