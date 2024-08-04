## https://huggingface.co/dalle-mini/vqgan_imagenet_f16_16384/discussions/6

contains_question: yes

question_part: please i wanted to ask a question, is it possible to reconstruct from indices that are not returned by the vqgan model, for instance, just to set a list containing integers like this: indices = jnp.array([[123, 334, 453, 554, 34, 53, 54]]), shape of indices is (1, 7), then try to decode it with vqgan_model.decode_code(indices). i tried it but it is returning InconclusiveDimensionOperation: Cannot divide evenly the sizes of shapes (1, 7, 256) and (1, 4, 4, -1).