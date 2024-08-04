### Documents:
- Evaluation scores

Hi,

Just out of curiosity. Do you have any evaluation scores (accuracy, f1-score, precision, recall)?
- Slightly better results than the reported results and some questions about the model

Hi there,

my colleague @dennlinger  and I are from the Institute of Computer Science at Heidelberg University, currently investigating the performance of German abstractive summarizers. We are very interested in your model and we have tested your model with the MLSUM Test set]() (all samples). We found that our results (see table below) are slightly better than the [results you reported in the model card.

| Parameters | Rouge2-precsion(mid) |Rouge2-recall(mid) |Rouge2-F1(mid) |
| ------ | ------ |------ |------ |
| MLSUM (max_length=354, min_length=13, do_sample=false, truncation=True) | 0.3334 | 0.3422 | 0.3347|


Besides, we have some further questions related to your model:

1. In the model page, we can not find any information about the evaluation parameters. Can you specify the hyperparameter choices that you used for the evaluation process?
2. You have trained your model for 18 epochs, which seems extremely long (given the dataset size). Have you evaluated the validation loss at all? Despite setting the `eval_steps`, `do_eval` is still set to `False`, which makes it unclear whether evaluation was performed during training.
3. We checked the first five articles in the test set and found that the summaries primarily (4/5 articles) consist of copies of the leading sentences of the reference articles. Also, the example summary output in the model page is just the first two sentences of the source text. Are you aware of this problem?

Thank you in advance for your response and input!

Best wishes,

Dennis and Jing
- Better results than the reported results and some questions about the model

Hi there,

my colleague @dennlinger  and I are from the Institute of Computer Science at Heidelberg University, currently investigating the performance of German abstractive summarizers. We are very interested in your model and have tested it (among others) on the MLSUM test set]() (all samples). In case you are interested, see the results listed in the table below, which indicates even better results than those [reported in the model card. 

| Parameters | Rouge1-F1 |Rouge2-F1 |RougeL-F1 |
| ------ | ------ |------ |------ |
| MLSUM (max_length=354, min_length=13, do_sample=false, truncation=True) | 0.4265 | 0.3321 | 0.3978|


Aside from this, we  have some further questions regarding the model and evaluation choices:

1. Why did you use the validation set instead of the test set for the evaluation?
2. The fine-tuned model was evaluated on 2000 random articles from the validation set. Did you use a seed in this process? Alternatively, could you share the subset of the 2000 articles that you used for the evaluation (IDs, etc.)?
3. Could you specify the hyperparameter choices that you used for the training and evaluation process? We were unable to load the `training_args.bin` file, potentially related to this issue.
4. We checked the first five articles in the test set and and found that the summaries primarily (4/5 articles) consist of copies of the leading sentences of the reference articles. Are you aware of this problem or did you perform any additional filtering?

Thank you in advance for your response and input!

Best wishes,

Dennis and Jing
### Keywords: evaluation, score, leaderboard, scores, benchmarks, results, accuracy, model, benchmark, humaneval