## https://huggingface.co/minimaxir/sdxl-wrong-lora/discussions/4

contains_question: yes

question_part: Getting this error on the latest colab. Looks like the layer string is `lora_unet_down_blocks_1_attentions_0_transformer_blocks_0_attn1_to_k.lora_down.weight` but the loader code doesn't have a case for `down_blocks` so it fails. Any ideas?