## https://huggingface.co/vinai/bertweet-base/discussions/2

contains_question: yes

question_part: Well, to adapt the BERTweetTokenizer for Portuguese we cloned the entire BERTweetTokenizer code and changed only one simple line of it:

Additionally what you would do if you needed to extend BERTweet to a different language? Would you do the same we did here creating a whole new .py file for a specific tokenizer language but actually changing on single line? (in fact, only passing a different parameter value)?