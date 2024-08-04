## https://huggingface.co/togethercomputer/StripedHyena-Nous-7B/discussions/2

contains_question: yes

question_part:
* Flash depth wise:
2) I'm not sure what package is intended but flashfftconv mentioned in github repo has `FlashDepthWiseConv1d` (upper case W)
3) If I use `from flashfftconv import FlashDepthWiseConv1d as FlashDepthwiseConv1d` and enable flash_depthwise in config I get warnings about unitialized parameters:

* flash fft
It's marked as compatible in yml file, but if I try to use it, model.py raises error