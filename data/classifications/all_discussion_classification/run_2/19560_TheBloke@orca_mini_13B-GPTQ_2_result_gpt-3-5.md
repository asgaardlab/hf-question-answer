## https://huggingface.co/TheBloke/orca_mini_13B-GPTQ/discussions/2

contains_question: yes
question_part: I noticed this model doesn't have ".g_idx" tensors, which apparently my inference code is looking for (latest source version of HF's text-generation-inference). Some of your other models do have them (like stable-vicuna-13B-GPTQ). I understand this possibly has something to do with GPTQ-for-LLaMa. Could anyone explain what these do at a high level? Is there a way to bypass this with my code or are these vital?