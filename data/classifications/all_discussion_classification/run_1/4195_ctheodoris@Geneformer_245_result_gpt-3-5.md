## https://huggingface.co/ctheodoris/Geneformer/discussions/245

contains_question: yes

question_part: I would like to run the model on GPU 1, 2, or 3. I've already tried to edit `in_silico_perturber.py` and have replaced every instance of `'cuda'` with `'cuda:1'`. However, it seems the model is still trying to run on GPU 0 (error posted at bottom).