## https://huggingface.co/Salesforce/codegen2-16B/discussions/1

contains_question: yes

question_part:
Why custom modeling code?
The `modeling_codegen.py` and `configuration_codegen.py` in this repo appear to just be older versions of those files from the transformers library. In particular they don't include recent fixes to `position_ids` support (for handling variable left-padding properly).
Can this section be removed from `config.json` (and the py files can then be removed too)?