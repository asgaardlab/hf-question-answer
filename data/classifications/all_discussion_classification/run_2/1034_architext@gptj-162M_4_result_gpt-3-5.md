## https://huggingface.co/architext/gptj-162M/discussions/4

contains_question: yes

question_part: Every time I try to use the model I get the following error.

RuntimeError: The size of tensor a (48) must match the size of tensor b (64) at non-singleton dimension 3

It happens also on the huggingface page in the test section of the model page.

I am new to ML, but to me it looks like internal problem that a model encounters when trying to parse the input I feed to it. This is an example string I use as input.

a house with two bedrooms and three bathrooms

I appreciate any ideas how one can fix this on the user side or any updates about possible fixes in the future =)