## https://huggingface.co/deepset/gbert-base-germandpr-reranking/discussions/2

contains_question: yes
question_part: Many Cross-Encoders take pairs of Question and Candidate Documents as input and deliver a single relevance score value from -10 ... +10 for each such pair (not related ... very relevant). There is also a model wrapper CrossEncoder in the Sentence Transformers package, that I'd like to use. I can use this CrossEncoder together with this model, but instead of single numbers i get pairs of numbers (Label0/Label1). Is Label1 the positive score (match) and i can use this as relevance score? Seems to work quite well...Or should I somehow combine this two values?, How is it trained, what does each of these 2 classification labels indicate? Another question: How well does it work on mixed German / English? Thx and best regards, André