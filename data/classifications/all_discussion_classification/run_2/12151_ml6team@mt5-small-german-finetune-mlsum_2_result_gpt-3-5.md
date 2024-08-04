## https://huggingface.co/ml6team/mt5-small-german-finetune-mlsum/discussions/2

contains_question: yes

question_part:
1. Why did you use the validation set instead of the test set for the evaluation?
2. The fine-tuned model was evaluated on 2000 random articles from the validation set. Did you use a seed in this process? Alternatively, could you share the subset of the 2000 articles that you used for the evaluation (IDs, etc.)?
3. Could you specify the hyperparameter choices that you used for the training and evaluation process? We were unable to load the `training_args.bin` file, potentially related to [this issue](https://discuss.huggingface.co/t/cannot-load-training-args-bin/10614).
4. We checked the first five articles in the test set and and found that the summaries primarily (4/5 articles) consist of copies of the leading sentences of the reference articles. Are you aware of this problem or did you perform any additional filtering?