## https://huggingface.co/mayaeary/pygmalion-6b_dev-4bit-128g/discussions/6

contains_question: yes
question_part: I've not managed to load the model in Oobabooga's Text Generation web UI.
For one thing, I don't know which loader to use. I've tried them all, but they've each found an error (not always a new error), and none managed to load the model, leading me to believe I may need to fidget with the loader settings as well. Found errors include " 'hidden_size'", "At least one of the model submodule will be offloaded to disk, please pass along an `offload_folder`" and "Trying to set a tensor of shape torch.Size([32, 512]) in "qzeros" (which has shape torch.Size([1, 512])), this look incorrect."
Any help would be much appreciated!