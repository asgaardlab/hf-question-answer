## https://huggingface.co/shi-labs/oneformer_coco_swin_large/discussions/2

contains_question: yes
question_part: In this case model return OneFormerModelOutput object and it's on GPU. model(**instance_inputs).to('cpu') doesn't work here. How can I return this object on CPU?