## https://huggingface.co/google/deplot/discussions/10

contains_question: yes
question_part: Fine Tuning and Both the Train AND Validation Loss Drop to Zero Extremely Quickly (within ~100 steps).
What Loss Function is the default inside this model?
I am concerned that the loss function may well suited to my Metric (Rouge L)?
Was Using Adam Optimizer with PyTorch Lightning, as When I tried to use AdaFactor with cosine scheduler I got a tonne of errors.
Am I getting stuck in a Local Minimum? And Should I work harder on integrating AdaFactor and Cosine Scheduling?