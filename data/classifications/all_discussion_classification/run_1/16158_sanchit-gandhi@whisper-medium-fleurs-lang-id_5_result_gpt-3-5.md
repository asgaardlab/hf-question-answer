## https://huggingface.co/sanchit-gandhi/whisper-medium-fleurs-lang-id/discussions/5

contains_question: yes

question_part: Hello 👋 
I was trying to lower the validation loss without success. I tried with different dropouts eg.: --attention_dropout 0.1 --dropout 0 —activation_dropout 0 and other variations. However what I observed is that with any dropout the training loss stops decreasing, and the evaluation loss reaches similar values as the training loss (they are both still high(60-80%)) however the accuracy is constant with low value (~50-60%).  Do you have any suggestions on which training parameters might help decrease the evaluation loss