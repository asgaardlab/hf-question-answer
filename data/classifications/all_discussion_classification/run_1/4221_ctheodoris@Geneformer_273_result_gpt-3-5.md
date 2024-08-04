## https://huggingface.co/ctheodoris/Geneformer/discussions/273

contains_question: yes

question_part: Example code for other fine-tuning applications (e.g. gene-level experiments, gene/drug perturbation)?
I was wondering if you may have plans to release code for other downstream tasks for Geneformer?
For example, I am greatly interested in gene-level tasks such as your gene network centrality tasks/chromatin dynamic/TF target identification, or dosage sensitivity.
I'm also thinking of applying your model on drug and gene perturbation experiments - I was wondering if those would be feasible (perhaps by training your model by 1) appending the perturbed genes or drug tokens at the beginning of the input, before the gene tokens that represent the single cell that is being perturbed, and 2) applying some type of "reconstruction error" between the predicted gene tokens at the output and the actual perturbed single-cell expression rank value encodings).