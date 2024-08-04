## https://huggingface.co/bigscience-data/sgpt-bloom-1b7-nli/discussions/1

contains_question: yes
question_part: I had use your command `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 accelerate launch /content/code/biencoder/nli_msmarco/sentence-transformers/examples/training/nli/training_nli_v2.py --model_name bigscience/bloom-560m --freezenonbias --train_batch_size 64 --lr 32e-5 --pooling weightedmean --wandb --wandbwatchlog gradients --gradcache --chunksize 4`
Should I modify something ? Another question, can the model be improved on french language by fine-tuning it  multilingual like it is described here: https://www.sbert.net/examples/training/multilingual/README.html