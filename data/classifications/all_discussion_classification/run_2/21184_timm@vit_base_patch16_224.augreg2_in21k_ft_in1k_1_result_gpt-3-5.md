## https://huggingface.co/timm/vit_base_patch16_224.augreg2_in21k_ft_in1k/discussions/1

contains_question: yes

question_part: May I know the training parameters for this model? For example, something like
```
./distributed_train.sh 4 /data/imagenet --model vit_base_patch16_224.augreg2_in21k_ft_in1k --sched cosine --epochs 150 --warmup-epochs 5 --lr 0.4 --reprob 0.5 --remode pixel --batch-size 256 --amp -j 4
```