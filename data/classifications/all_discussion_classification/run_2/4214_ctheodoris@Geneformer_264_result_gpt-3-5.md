## https://huggingface.co/ctheodoris/Geneformer/discussions/264

contains_question: yes  
question_part: The error I got looks like:  
nf is not present in the dataset's disease attribute.  
Traceback (most recent call last):  
  File "/home/Geneformer/in_silico_perturbation.py", line 66, in <module>  
    isp.perturb_data("./fine_tuned_models/geneformer-6L-30M_CellClassifier_cardiomyopathies_220224",  
  File "/home/Geneformer/geneformer/in_silico_perturber.py", line 965, in perturb_data  
    raise  
RuntimeError: No active exception to reraise