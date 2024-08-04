## https://huggingface.co/stabilityai/stable-diffusion-2/discussions/41

contains_question: yes

question_part: Hey guys! 

I've been trying to load the stable-diffusion-2 model in the img2img pipeline, 

I've tried: 

model_path = "stabilityai/stable-diffusion-2"

pipe_img = StableDiffusionImg2ImgPipeline.from_pretrained(
    model_path,
    revision="fp16", 
    torch_dtype=torch.float16,
    use_auth_token=True
)

but this give the errors:

ValueError: Pipeline <class 'diffusers.pipelines.stable_diffusion.pipeline_stable_diffusion_img2img.StableDiffusionImg2ImgPipeline'> expected {'unet', 'scheduler', 'feature_extractor', 'vae', 'safety_checker', 'text_encoder', 'tokenizer'}, but only {'unet', 'scheduler', 'vae', 'text_encoder', 'tokenizer'} were passed.


which makes me believe there is another model for this, if available?