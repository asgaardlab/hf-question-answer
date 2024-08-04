## https://huggingface.co/projecte-aina/FLOR-6.3B/discussions/3

contains_question: yes

question_part: When trying to convert using the following command
```python
python3 convert-hf-to-gguf.py --outtype f16 /media/psf/2TB/Software/AI/Models/FLOR-6.3B
```

It outputs the following error message:

```Loading model: FLOR-6.3B
Traceback (most recent call last):
  File "/home/christopher/llama.cpp/convert-hf-to-gguf.py", line 1054, in <module>
    model_class = Model.from_model_architecture(hparams["architectures"][0])
                                                ~~~~~~~^^^^^^^^^^^^^^^^^
KeyError: 'architectures'```