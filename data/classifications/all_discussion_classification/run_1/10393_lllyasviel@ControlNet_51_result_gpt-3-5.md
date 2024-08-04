## https://huggingface.co/lllyasviel/ControlNet/discussions/51

contains_question: yes
question_part: My questions, therefore, are as follows:

1. Do I understand correctly that what we do is train the model without any weighting, and then for the ϵ_uc we use unconditional SD without ControlNet, and for ϵ_c we use ControlNet but before adding the skip connection, we multiply the output by wi (meaning SD_Layer_i_final_output = SD_Layer_i_output + (w_i*ControlNet_Layer_i_output) )?
2. If so, what is the logic and motivation for doing that? It doesn't sound trivial that this would be want we want to do.
3. Finally, I'd like to know where is this implemented in the code?