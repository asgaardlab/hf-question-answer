## https://huggingface.co/jinaai/jina-embeddings-v2-base-en/discussions/24

contains_question: yes

question_part: I fine-tuned the model on my data with `SentenceTransformers` library, but obviously just model.save() does not work (it saves without errors, but when I reload in next session - I get a `Some weights of BertModel were not initialized from the model checkpoint at ... and are newly initialized`) Can you please help, how can I save and reload the model (ideally with `SentenceTransformers` library)