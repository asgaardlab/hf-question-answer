## https://huggingface.co/ctheodoris/Geneformer/discussions/280

contains_question: yes

question_part: If we consider a token vector of 2048 genes for one cell, from the code it seems that when doing knockout of one gene, the corresponding token is removed from the vector. So the new vector after KO has now 2047 tokens and then it's padded to 2048. Am I reading the code correctly?  If so, I was wondering if it makes sense instead to store the entire gene vector even if it's longer than 2048, remove the target gene, then slice the resulting vector up to 2048. This way the last token would be the first gene that was left out by the first vector slicing during tokenization.  I was curious to know your opinion about the two approaches, and if you think one is to be preferred over the other.