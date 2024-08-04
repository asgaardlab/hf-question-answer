## https://huggingface.co/ml6team/keyphrase-extraction-kbir-inspec/discussions/3

contains_question: yes
question_part: Can you explain to me why for an empty input, the dimensionality of the hidden_state is torch.Size([25, 1, 2, 1024])?
As far as i can see the encoder Robertaencoder has 24*RobertaLayer, where is the 25 coming from?
Shouldnt the dimensionality be num_hidden_layers * 1 * tokens * hidden_size