## https://huggingface.co/NousResearch/Yarn-Mistral-7b-128k/discussions/10

contains_question: yes

question_part: I try:
``` 
python -u -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --model NousResearch/Yarn-Mistral-7b-128k --trust-remote-code
``` 

and i get:
``` 
  File "/home/azureuser/.local/lib/python3.10/site-packages/vllm/model_executor/layers/attention.py", line 266, in forward
    self.multi_query_kv_attention(
  File "/home/azureuser/.local/lib/python3.10/site-packages/vllm/model_executor/layers/attention.py", line 117, in multi_query_kv_attention
    key = torch.repeat_interleave(key, self.num_queries_per_kv, dim=1)
RuntimeError: CUDA error: an illegal memory access was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

Any idea about how to fix that?