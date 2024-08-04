## https://huggingface.co/HuggingFaceM4/idefics-9b-instruct/discussions/12

contains_question: yes  
question_part: I'm coming accross an error while trying to load the idefics-9b-instruct model. Even after downloading the model weights and loading them using `model = IdeficsForVisionText2Text.from_pretrained(model_path, torch_dtype=torch.bfloat16).to("cuda:1")` I'm getting this error:  
`OSError: Error no file named pytorch_model.bin, tf_model.h5, model.ckpt.index or flax_model.msgpack found in directory model_dir/idefics_9b/.`  