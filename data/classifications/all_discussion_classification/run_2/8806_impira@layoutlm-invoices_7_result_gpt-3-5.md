## https://huggingface.co/impira/layoutlm-invoices/discussions/7

contains_question: yes

question_part: I have been searching for ways to fine-tune the model for discontinuous tokens, the existing transformer-based pipeline only supports a single start and single end that is suitable for continuous sequences of tokens. But in the case of entities like addresses (as shown in the model card) this logic does not suffice. Any lead regarding how to train and get inference in such scenario will be much appreciated. Also, I've been trying this model with the same example as shown in the model card but still, it extracts only one line of address. Is it related to the prompt I am supplying or something else?