## https://huggingface.co/tuner007/pegasus_paraphrase/discussions/5

contains_question: yes

question_part: Hi

I am wondering if it can support using the new XLA text generation.

I followed this blog: https://huggingface.co/blog/tf-xla-generate

And used the following code

```python
from transformers import AutoModelForSeq2SeqLM , AutoTokenizer
import tensorflow as tf

from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()

ph_model_name = "tuner007/pegasus_paraphrase"

# torch_device = "cuda:0"
ph_tokenizer = AutoTokenizer.from_pretrained(ph_model_name)
ph_model = AutoModelForSeq2SeqLM.from_pretrained(ph_model_name)

tokenization_kwargs = {"max_length": 512, "padding": "longest", "truncation": True, "return_tensors": "tf"}
generation_kwargs = {"num_beams": 7, "max_length": 512,
                     "num_return_sequences":2, "temperature":0.7,
                     "do_sample": True, "top_k": 90, "top_p": 0.95,
                     "no_repeat_ngram_size": 2, "early_stopping": True}

# generate a paraphrased text
xla_generate = tf.function(ph_model.generate, jit_compile=True)

input_prompt = 'the world has been inching toward fully autonomous cars for years .'
tokenized_inputs = ph_tokenizer([input_prompt], **tokenization_kwargs)

generated_text = xla_generate(**tokenized_inputs, **generation_kwargs)
decoded_text = ph_tokenizer.decode(generated_text[0], skip_special_tokens=True)

print(decoded_text)
```

but got this error message

```python
TypeError                                 Traceback (most recent call last)
<ipython-input-8-a25ee9d320ec> in <module>
      1 input_prompt = 'the world has been inching toward fully autonomous cars for years .'
      2 tokenized_inputs = ph_tokenizer([input_prompt], **tokenization_kwargs)
----> 3 generated_text = xla_generate(**tokenized_inputs, **generation_kwargs)
      4 decoded_text = ph_tokenizer.decode(generated_text[0], skip_special_tokens=True)
      5 print(decoded_text)

1 frames
/usr/local/lib/python3.7/dist-packages/tensorflow/python/framework/func_graph.py in autograph_handler(*args, **kwargs)
   1145           except Exception as e:  # pylint:disable=broad-except
   1146             if hasattr(e, "ag_error_metadata"):
-> 1147               raise e.ag_error_metadata.to_exception(e)
   1148             else:
   1149               raise

TypeError: in user code:

    File "/usr/local/lib/python3.7/dist-packages/torch/autograd/grad_mode.py", line 847, in decorate_context  *
        return func(*args, **kwargs)
    File "/usr/local/lib/python3.7/dist-packages/transformers/generation_utils.py", line 1182, in generate  *
        model_kwargs = self._prepare_encoder_decoder_kwargs_for_generation(
    File "/usr/local/lib/python3.7/dist-packages/transformers/generation_utils.py", line 525, in _prepare_encoder_decoder_kwargs_for_generation  *
        model_kwargs["encoder_outputs"]: ModelOutput = encoder(**encoder_kwargs)
    File "/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py", line 1130, in _call_impl  *
        return forward_call(*input, **kwargs)
    File "/usr/local/lib/python3.7/dist-packages/transformers/models/pegasus/modeling_pegasus.py", line 753, in forward  *
        input_shape = input_ids.size()

    TypeError: 'numpy.int64' object is not callable

Any help?