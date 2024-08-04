## https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/discussions/15

contains_question: yes

question_part: <Users/sachin/ai/llamaindex-openllm/llamaindex-openllm/lib/python3.10/site-packages/transformers/generation/utils.py:2920: UserWarning: MPS: no support for int64 for min_max, downcasting to a smaller data type (int32/float32). Native support for int64 has been added in macOS 13.3. (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/aten/src/ATen/native/mps/operations/ReduceOps.mm:621.)  
if unfinished_sequences.max() == 0:  
>>>   
But I get nothing in the output or any error beyond the warnings above:
>>> outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)  
>>> print(outputs[0]["generated_text"])  
<|system|>  
You are a friendly chatbot who always responds in the style of a pirate</s>  
<|user|>  
How many helicopters can a human eat in one sitting?</s>  
<|assistant|>