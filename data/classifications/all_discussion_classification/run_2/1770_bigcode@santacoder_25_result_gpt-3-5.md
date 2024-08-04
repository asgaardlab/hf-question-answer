## https://huggingface.co/bigcode/santacoder/discussions/25

contains_question: yes

question_part: MBPP provides text instructions, e.g. "Write a function to reverse words in a given string.", which the SantaCoder model card explicitly advises against using. Nevertheless, I try to prompt the model in one of two ways (in Python):
1) Function signature, followed by docstring:
```
def reverse_words(s):
    """Write a function to reverse words in a given string."""
```
2) Comment, followed by function signature
```
# Write a function to reverse words in a given string.
def reverse_words(s):
```
Should I change the prompting method, or is this output acceptable and I should just truncate the output manually? I am trying to reproduce the eval results from the paper as closely as possible. Thanks for your help.