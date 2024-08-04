## https://huggingface.co/segmind/SSD-1B/discussions/19

contains_question: yes

question_part: Hi, ModelSpec https://github.com/Stability-AI/ModelSpec is used to easily identify key data about singlefile models, and is missing from your SSD-1B.safetensors model - this means that, keywise, it will be assumed by parsers to be an SDXL 0.9 Preview model (as it matches the SDXL keys, but lacks the SDXL 1.0 ModelSpec metadata nor its own metadata).

For example, here's how SSD-1B looks next to the SDXL 1.0 models in StableSwarmUI's model browser:

![image.png](https://cdn-uploads.huggingface.co/production/uploads/64c12d35cac5f9ba52b68720/qXeurYA19CWjBVn2igv2z.png)


So I'm requesting that you add ModelSpec metadata. Probably the 'modelspec.architecture' key should be 'segmind-stable-diffusion-1b'.

I'm happy to provide more information if needed.