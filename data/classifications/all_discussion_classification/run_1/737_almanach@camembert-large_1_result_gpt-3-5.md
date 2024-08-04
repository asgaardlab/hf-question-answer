## https://huggingface.co/almanach/camembert-large/discussions/1

contains_question: yes
question_part: The `truncation=True` parameter with camembert-large's tokenizer does not seem to have any effect. When running this example: "Asking to truncate to max_length but no maximum length is provided and the model has no predefined maximum length. Default to no truncation. The inference thus causes an exception on long sentences because the tokenizer fails to truncate the input to 512 tokens."