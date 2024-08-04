### Documents:
- Loading llama-13b using 'AutoTokenizer, AutoModelForCausalLM'

I am trying loading this tokenizer and model using the below code:
'''
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("")
model = AutoModelForCausalLM.from_pretrained("")
'''

However it gives me the error :
'''
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
/tmp/ipykernel_1596897/927730692.py in <module>
      8 
      9 # Instantiate a text-generation pipeline
---> 10 text_generator = pipeline("text-generation", model="circulus/llama-13b")
     11 
     12 # Generate text using the model

~/.local/lib/python3.10/site-packages/transformers/pipelines/__init__.py in pipeline(task, model, config, tokenizer, feature_extractor, image_processor, framework, revision, use_fast, use_auth_token, device, device_map, torch_dtype, trust_remote_code, model_kwargs, pipeline_class, **kwargs)
    690         hub_kwargs["_commit_hash"] = config._commit_hash
    691     elif config is None and isinstance(model, str):
--> 692         config = AutoConfig.from_pretrained(model, _from_pipeline=task, **hub_kwargs, **model_kwargs)
    693         hub_kwargs["_commit_hash"] = config._commit_hash
    694 

~/.local/lib/python3.10/site-packages/transformers/models/auto/configuration_auto.py in from_pretrained(cls, pretrained_model_name_or_path, **kwargs)
    915             return config_class.from_pretrained(pretrained_model_name_or_path, **kwargs)
    916         elif "model_type" in config_dict:
--> 917             config_class = CONFIG_MAPPING[config_dict["model_type"]]
    918             return config_class.from_dict(config_dict, **unused_kwargs)
    919         else:

~/.local/lib/python3.10/site-packages/transformers/models/auto/configuration_auto.py in __getitem__(self, key)
    621             return self._extra_content[key]
    622         if key not in self._mapping:
--> 623             raise KeyError(key)
    624         value = self._mapping[key]
    625         module_name = model_type_to_module_name(key)

KeyError: 'llama'
'''
Which suggest it cannot find the model and tokenizer.
May I ask what is the correct way to import the model from hugging face and run it , without downloading it to my local machine?

Many thanks!
- can this model run on cpu, I had a error when I test it on cpu, this with a error about should install flash_attn

test code:
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

#model = AutoModelForCausalLM.from_pretrained("./model", low_cpu_mem_usage=True, device_map="cpu", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("./model", torch_dtype=torch.float16, device_map="cpu", trust_remote_code=True)
tok = AutoTokenizer.from_pretrained("./model").to("cpu")
x
= tok.encode("The mistral wind in is a phenomenon ", return_tensors="pt")
x = model.generate(x, max_new_tokens=128)
print(tok.batch_decode(x))

error message:
/home//.local/lib/python3.10/site-packages/torch/onnx/_internal/_beartype.py:30: UserWarning: module 'beartype.roar' has no attribute 'BeartypeDecorHintPep585DeprecationWarning'
  warnings.warn(f"{e}")
Traceback (most recent call last):
  File "/home//04_files/Model/mixtral/./test0.py", line 5, in <module>
    model = AutoModelForCausalLM.from_pretrained("./model", torch_dtype=torch.float16, device_map="cpu", trust_remote_code=True)
  File "/home//.local/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py", line 553, in from_pretrained
    model_class = get_class_from_dynamic_module(
  File "/home//.local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 488, in get_class_from_dynamic_module
    final_module = get_cached_module_file(
  File "/home//.local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 315, in get_cached_module_file
    modules_needed = check_imports(resolved_module_file)
  File "/home//.local/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 180, in check_imports
    raise ImportError(
ImportError: This modeling file requires the following packages that were not found in your environment: flash_attn. Run `pip install flash_attn`
I tried to install flash_attn ,but it cannot install succ without a cuda driver, so this model cannot work on cpu now?
- Problem in loading falcon-7b-instruct locally

I have  downloaded and saved the "falcon-7b-instruct" model files to your local machine (Windows 10 OS with 16 GB RAM and 1 TB SSD). But when i am trying to load model i am getting below error.

Traceback (most recent call last):
  File "d:\qlora\models\bot.py", line 5, in <module>
    tokenizer = AutoTokenizer.from_pretrained(model_directory)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\yashwank\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\models\auto\tokenization_auto.py", line 666, in from_pretrained
    config = AutoConfig.from_pretrained(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\yashwank\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\models\auto\configuration_auto.py", line 958, in from_pretrained
    trust_remote_code = resolve_trust_remote_code(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\yashwank\AppData\Local\Programs\Python\Python311\Lib\site-packages\transformers\dynamic_module_utils.py", line 535, in resolve_trust_remote_code
    signal.signal(signal.SIGALRM, _raise_timeout_error)
                  ^^^^^^^^^^^^^^
AttributeError: module 'signal' has no attribute 'SIGALRM'. Did you mean: 'SIGABRT'?


****************Code i am trying to load model******************
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_directory = "path/to/your/model/directory"

tokenizer = AutoTokenizer.from_pretrained(model_directory)
model = AutoModelForCausalLM.from_pretrained(model_directory)

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
..............so on

Am i doing anything wrong? How to fix this?
### Keywords: layers, model layers, model, transformers, self_attn, error, bias, py, file, from_pretrained