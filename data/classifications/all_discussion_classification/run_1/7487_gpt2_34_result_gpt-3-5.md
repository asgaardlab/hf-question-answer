## https://huggingface.co/gpt2/discussions/34

contains_question: yes
question_part: I have a question about how to properly train a GPT-2-like transformer for a causal LM task. This question applies to both fine-tuning and training a model from scractch.
My question is basically: is this approach with using a `DataCollatorForLanguageModeling` instance + adding the special padding token correct / good practice? Or should I be using the `default_data_collator` and restructuring my dataset prior to training? Aren't they supposed to be functionally equivalent approaches?