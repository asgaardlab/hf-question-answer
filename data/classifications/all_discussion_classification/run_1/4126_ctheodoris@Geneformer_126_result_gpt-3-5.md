## https://huggingface.co/ctheodoris/Geneformer/discussions/126

contains_question: yes
question_part: I'm currently trying to analyze the cell embedding and I'm not sure I understand the extraction of cell embedding correctly.
The last layer I got from the model.predict should be batch_size x 2048 x 256 matrix, right? So I need to average across gene dimension to get a matrix of batch_size x 256, which would be my cell embedding. I'm wondering do the dimension of gene still represent the input length? Since in the input if a cell got less gene than 2048, there will be padding filled into the input.
In other words, do we add all numbers in the gene dimension and divide by 2048 or we should divide it by the number of gene that the current cell actually has (for example, maybe we only detect 2000 genes in that cell and we should divide the result by 2000)