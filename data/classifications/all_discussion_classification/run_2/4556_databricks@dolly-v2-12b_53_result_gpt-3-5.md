## https://huggingface.co/databricks/dolly-v2-12b/discussions/53

contains_question: yes
question_part: if a PCA produces vectors that are optimised for searching then can we not take a parent model, do PCA on the vector embeddings of a model's training data, with or without reducing dimensions, to obtain the transformation matrix from one coordinate system to the other, and then train a student language model using the PCA-optimised embedding dimensions.