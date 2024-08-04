## https://huggingface.co/OFA-Sys/ofa-base/discussions/1

contains_question: yes

question_part: Is there a way to do few shot inference or batch inference? (with the hugging face generator) I tried doing batch by adding another string to the inputs making it size [2,x] and batched images to make the size [2,3,480,480] but i was getting this error "1191 if patch_images_2 is not None: 1192 image_embed_2, image_num_patches_2, image_padding_mask_2, image_position_ids_2, image_pos_embed_2 = \ 1193 self.get_patch_images_info(patch_images_2, sample_patch_num, input_ids.device)