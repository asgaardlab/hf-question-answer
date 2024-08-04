## https://huggingface.co/bigscience/bloomz/discussions/51

contains_question: yes
question_part: Hello, why doesn't the nomenclature of the modules in the Bloom and Bloomz models adhere to those created by the BloomPreTrainedModel class: base_model_prefix = "transformer"? The issue is that in TGI, which has adapted to Bloom modeling, models trained by Transformers do not work because the TGI library looks for model names without the "transformer" prefix.