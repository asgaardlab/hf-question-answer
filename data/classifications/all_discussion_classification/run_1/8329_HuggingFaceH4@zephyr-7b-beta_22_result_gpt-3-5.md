## https://huggingface.co/HuggingFaceH4/zephyr-7b-beta/discussions/22

contains_question: yes

question_part: However, when I tried to fine-tune a smaller model (to learn the concept) following this [tutorial](https://github.com/huggingface/trl/tree/main/examples/scripts). I got a different trend:
```
Validation Loss ↓
Rewards/chosen ↑
Rewards/rejected ↑
Rewards/accuracies ↑ 
Rewards/margins ↑
```
I am only tuning with different `learning_rate` now and my model can't achieve a trend in yours. May I ask which trend is correct and if there is any secret recipe behind it?