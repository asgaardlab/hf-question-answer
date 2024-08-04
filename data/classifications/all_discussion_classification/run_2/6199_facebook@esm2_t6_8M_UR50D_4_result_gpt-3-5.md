## https://huggingface.co/facebook/esm2_t6_8M_UR50D/discussions/4

contains_question: yes

question_part: Looks likes indeed the function `dispatch_model` does not have an 'offload_index'. I tried removing `offload_index` from the function call, it crashed my server 😂. Also, It seems that I cannot even generate a device map for the Facebook ESM model. Any thoughts about the issue above would be greatly appreciated.