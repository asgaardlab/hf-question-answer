## https://huggingface.co/openaccess-ai-collective/phi-platypus-qlora/discussions/1

contains_question: yes

question_part: Seems I'm getting the same error with this model too...  [adapted gist from here](https://gist.github.com/TheBloke/d31d289d3198c24e0ca68aaf37a19032) from @TheBloke 

@teknium seems to have figured it out? perhaps this issue is some bug in config of qlora?

`
RuntimeError: Error(s) in loading state_dict for MixFormerSequentialForCausalLM:
	size mismatch for layers.25.linear.lora_B.default.weight: copying a param with shape torch.Size([50304, 64]) from checkpoint, the shape in current model is torch.Size([51200, 64]).
`
note: only occurs on the final layer!?....