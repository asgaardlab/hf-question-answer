## https://huggingface.co/tuhailong/cross-encoder-bert-base/discussions/2

contains_question: yes

question_part: From sbert cross encoder page, I find two train example, [one](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/cross-encoder/training_stsbenchmark.py), [two](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/ms_marco/train_cross-encoder_scratch.py). While one use CECorrelationEvaluator, two use CERerankingEvaluator. I want use cross encoder to ranking the search items, which way should i use. From word meaning i think reranking maybe more suitable. But it's label only has 0/1. correlation's label could be number represent the relevance between query and doc.