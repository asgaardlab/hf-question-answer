## https://huggingface.co/deutsche-telekom/mt5-small-sum-de-mit-v1/discussions/1

contains_question: yes

question_part: 
1. For the data preprocessing, only the records with no more than 94 summary tokens were selected. Could we ask why you chose 94? Is this somehow related to the SwissText dataset?
2. As a follow-up, did you also perform similar filtering on the validation and test set (potentially explaining the different results we obtain)?
3. There are no parameters specified for the generation of summaries in the test set (aside from "no beams"). Does this imply that you simply performed greedy search for the summary without specification of any further parameters (like minimum/maximum length)?
4. We randomly checked some source articles and the generated summaries and have found that there is frequent repetition and semantic incoherence in the generated summaries. The following figure is an example of the first five articles in the MLSUM test set for your model's output. Do you have any insights into why this might occur?