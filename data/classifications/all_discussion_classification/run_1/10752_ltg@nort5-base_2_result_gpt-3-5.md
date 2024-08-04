## https://huggingface.co/ltg/nort5-base/discussions/2

contains_question: yes

question_part: I get the message ```AttributeError: 'function' has no attribute 'forward'```. I believe this is because the ```get_encoder``` function in ```NorT5Model``` returns the ```get_encoder_output``` function, not an object.  I've tried to write an encoder wrapper around the ```Encoder``` class which implements the ```get_encoder_output``` function as its ```forward``` function, but then I get an issue with the shape of ```input_shape```, so maybe this is the wrong way around. Any help?