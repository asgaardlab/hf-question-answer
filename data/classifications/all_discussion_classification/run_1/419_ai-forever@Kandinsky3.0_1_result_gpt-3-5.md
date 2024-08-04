## https://huggingface.co/ai-forever/Kandinsky3.0/discussions/1

contains_question: yes

question_part: 
1. Why does this model require more resources than original one? https://huggingface.co/kandinsky-community/kandinsky-3
2. Why do you download `kandinsky3.pt` and `movq.pt` each time instead of loading from hf cache directory?
3. Where do you store `kandinsky3.pt` and `movq.pt`?
4. How to run the inference on RTX 4090? I was barely able to load it adding more RAM, but the inference does not work, even distribute on 2 RTX 4090 like this:

```python
import torch
from accelerate import PartialState
from diffusers import DiffusionPipeline

distributed_state = PartialState()
distributed_state.num_processes = 2

t2i_pipe = get_T2I_pipeline(distributed_state.device, fp16=True)
```
Inference on A100 is horribly slow...