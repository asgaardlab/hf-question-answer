## https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/discussions/28

contains_question: yes

question_part: StableDiffusionXLPipeline.from_pretrained use_safetensors=True is downloading onnx models

Why is 
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
)

Downloaded onnx models and not safetensors ?