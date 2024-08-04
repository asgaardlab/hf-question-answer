## https://huggingface.co/Salesforce/codet5-small/discussions/2

contains_question: yes
question_part: According to the CodexGlue dataset format, you expect a list of codes and you return the top n most similar examples to a given query. But what if I want to check the similarity between two specific code snippets? How can I use your model for that?
Can you please provide a way to get a similarity score (maybe a probability) or a binary output (0 or 1) if two code snippets are similar or different? For example, given these two code snippets:
```
public int f() { return 0;}
```
```
public void f() { int i = 0; }
```
Can your model tell me how similar they are, or if they are equivalent or not?