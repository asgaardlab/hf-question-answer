## https://huggingface.co/deepset/gbert-base-germandpr-reranking/discussions/2

contains_question: yes

question_part: 
question - many Cross-Encoders take pairs of Question and Candidate Documents as input and deliver a single relevance score value from -10 ... +10 for each such pair (not related ... very relevant).
Or should I somehow combine this two values? A bit more documentation would be great, because not everyone want to use the full Haystack/FARM-stack and just want to use the model itself, e.g. via a seperate Inference Server etc.
How is it trained, what does each of these 2 classification labels indicate?
How well does it work on mixed German / English?