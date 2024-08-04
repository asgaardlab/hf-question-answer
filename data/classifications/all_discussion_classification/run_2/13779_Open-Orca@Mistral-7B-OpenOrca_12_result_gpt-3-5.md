## https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/discussions/12

contains_question: yes
question_part: This problem has ocurred to me multiple times when testing 7B-models. When I ask the model to draft me a short agreement, it does so wothout numbering the individual clauses. Upon asking the model to number the clauses, it complies with the question, but gives me an answer like this:

"Sure! Here's the revised version of the contract with points numbered for easier understanding:"

It does not continue, although the max token length is set to 2000. Under some circumstances I do not understand, the model seems to be incapable of numbering. I never had this issue with a 13B-model.