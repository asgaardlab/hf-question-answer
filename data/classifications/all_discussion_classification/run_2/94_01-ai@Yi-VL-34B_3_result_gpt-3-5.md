## https://huggingface.co/01-ai/Yi-VL-34B/discussions/3

contains_question: yes

question_part: 
Great work! However, it seems like your model is incompatible with LLava's inference code, which contradicts what you mentioned in the readme. A ValueError is raised when loading your model with llava's code. The full trace log is listed below: 
I looked into the builder.py in llava's repo, and found that your projector type `mlp2x_gelu_Norm` is not supported https://github.com/haotian-liu/LLaVA/blob/9a26bd1435b4ac42c282757f2c16d34226575e96/llava/model/multimodal_projector/builder.py#L39 
Besides, I'm confused that there is no "mm_projector.bin" in your model files, which is basically not supported by llava's model loading logic. Looking forward to your reply!