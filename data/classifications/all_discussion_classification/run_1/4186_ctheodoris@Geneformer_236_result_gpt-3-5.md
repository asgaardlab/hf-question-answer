## https://huggingface.co/ctheodoris/Geneformer/discussions/236

contains_question: yes
question_part: what does "/path/to/miniconda3/lib:/path/to/sw/lib:/path/to/sw/lib" refer to? 
However, when I use "anaconda3", how can I identify the "/path/to" and "sw/lib" in my own environment?
Besides, why was the "/path/to/sw/lib" repeated twice? Is this related to some specific configuration?
I'm still tortured by constant " Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False." from serialization.py and registry.py when running hyperparam_optimiz_for_disease_classifier.py, though "print(torch.cuda.is_available())" can return true separately. I wonder whether this problem can be caused by wrongly set runtime_env and os.environ.