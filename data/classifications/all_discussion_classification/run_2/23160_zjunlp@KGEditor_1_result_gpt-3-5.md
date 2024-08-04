## https://huggingface.co/zjunlp/KGEditor/discussions/1

contains_question: yes

question_part: 
1. What is the correspondence between entity and ENTITY_id in add_tokens.json?  and the relation to RELATION_ID?
2. And the input for each model is "[CLS][ENTITY_i][SEP][RELATION_i][SEP][MASK][SEP]"  or "[CLS][ENTITY_i][RELATION_i][MASK][SEP]"  and use [MASK] as the query?
3.When we use [MASK] to do prediction, how many categories are there? Only the Number of entities OR the number of entities+Bert's original vocabulary size?