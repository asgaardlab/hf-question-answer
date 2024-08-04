## https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt/discussions/8

contains_question: yes

question_part: Therefore I wanted to gain the attention_scores but when using model.generate(**encoded_hi, forced_bos_token_id=tokenizer.lang_code_to_id["de_DE"], output_attentions=True, output_hidden_states=True) print(generated_tokens) only the generated tokes and no attentions are returned. 