## https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler/discussions/8

contains_question: yes

question_part: I get this error running the latest diffusers version `0.13.0.dev0`:
```
/home/jonno/diffusers/src/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion_upscale.py:104: FutureWarning: The configuration file of the vae does not contain `scaling_factor`
 or it is set to 0.18215, which seems highly unlikely. If your checkpoint is a fine-tuned version of `stabilityai/stable-diffusion-x4-upscaler` you should change 'scaling_factor' to 0.08333 
Please make sure to update the config accordingly, as not doing so might lead to incorrect results in future versions. If you have downloaded this checkpoint from the Hugging Face Hub, 
it would be very nice if you could open a Pull Request for the `vae/config.json` file
  deprecate("wrong scaling_factor", "1.0.0", deprecation_message, standard_warn=False)
```