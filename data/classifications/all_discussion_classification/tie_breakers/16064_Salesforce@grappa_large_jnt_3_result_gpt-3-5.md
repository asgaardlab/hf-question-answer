## https://huggingface.co/Salesforce/grappa_large_jnt/discussions/3

contains_question: yes

question_part: OSError: Can't load config for 'Salesforce/grappa_large_jnt'
I am not able to import the model. I am using transformers 4.5.1. When I try to run

from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("Salesforce/grappa_large_jnt")
model = AutoModelForMaskedLM.from_pretrained("Salesforce/grappa_large_jnt")

I get the following error:

OSError: Can't load config for 'Salesforce/grappa_large_jnt'. Make sure that:
- 'Salesforce/grappa_large_jnt' is a correct model identifier listed on 'https://huggingface.co/models'
- or 'Salesforce/grappa_large_jnt' is the correct path to a directory containing a config.json file

I am operating on a remote server, so I cant simply download all model files via a browser interface. What can I do?