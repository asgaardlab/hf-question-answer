## https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/discussions/28

contains_question: yes

question_part: Why is 
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
)

Downloaded onnx models and not safetensors ?