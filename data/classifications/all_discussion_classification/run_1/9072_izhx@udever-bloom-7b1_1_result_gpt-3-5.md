## https://huggingface.co/izhx/udever-bloom-7b1/discussions/1

contains_question: yes

question_part: 
I'm interested in running this using the MLX framework, but intelligently converting weights is beyond my understanding currently.
Does anyone have any guidance on getting this working, or steps to understand how to go about converting something like this to work with mlx?
I kind of get the whole `mx.array` thing, but how do you reason about converting weights?
There is a Bert example - https://github.com/ml-explore/mlx-examples/tree/main/bert
With the conversion script being - https://github.com/ml-explore/mlx-examples/blob/10a7b99e835b87b9f6d762fcb4de47b6f300f52e/bert/convert.py#L22
Seems mostly to be replacing a few keys, but what's the rationale? Is that just the tensor -> npz format stuff? Are there any other considerations?