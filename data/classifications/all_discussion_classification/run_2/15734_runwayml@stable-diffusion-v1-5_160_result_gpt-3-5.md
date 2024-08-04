## https://huggingface.co/runwayml/stable-diffusion-v1-5/discussions/160

contains_question: yes

question_part: It throws inside 'load_sub_module':
```
ValueError: Cannot load <class 'diffusers.models.autoencoder_kl.AutoencoderKL'> from /fsx/cld-models/stable-diffusion/1/vae because the following keys are missing: 
 decoder.mid_block.attentions.0.proj_attn.weight, encoder.mid_block.attentions.0.key.weight, encoder.mid_block.attentions.0.proj_attn.bias, decoder.mid_block.attentions.0.value.weight, decoder.mid_block.attentions.0.key.bias, decoder.mid_block.attentions.0.query.weight, encoder.mid_block.attentions.0.query.bias, encoder.mid_block.attentions.0.proj_attn.weight, decoder.mid_block.attentions.0.proj_attn.bias, encoder.mid_block.attentions.0.key.bias, decoder.mid_block.attentions.0.key.weight, encoder.mid_block.attentions.0.query.weight, decoder.mid_block.attentions.0.value.bias, decoder.mid_block.attentions.0.query.bias, encoder.mid_block.attentions.0.value.weight, encoder.mid_block.attentions.0.value.bias. 
 Please make sure to pass `low_cpu_mem_usage=False` and `device_map=None` if you want to randomly initialize those weights or else make sure your checkpoint file is correct.
```