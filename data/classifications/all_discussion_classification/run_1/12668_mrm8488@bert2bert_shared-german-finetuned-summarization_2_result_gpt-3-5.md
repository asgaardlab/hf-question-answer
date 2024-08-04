## https://huggingface.co/mrm8488/bert2bert_shared-german-finetuned-summarization/discussions/2

contains_question: yes

question_part: 
1. In the [model page](https://huggingface.co/mrm8488/bert2bert_shared-german-finetuned-summarization), we can not find any information about the evaluation parameters. Can you specify the hyperparameter choices that you used for the evaluation process?
2. You have trained your model for 18 epochs, which seems extremely long (given the dataset size). Have you evaluated the validation loss at all? Despite setting the `eval_steps`, `do_eval` is still set to `False`, which makes it unclear whether evaluation was performed during training.
3. We checked the first five articles in the test set and found that the summaries primarily (4/5 articles) consist of copies of the leading sentences of the reference articles. Also, the example summary output in the [model page](https://huggingface.co/mrm8488/bert2bert_shared-german-finetuned-summarization) is just the first two sentences of the source text. Are you aware of this problem?