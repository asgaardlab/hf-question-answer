## https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ/discussions/5

contains_question: yes

question_part: Getting ```ValueError: OC is not a multiple of cta_N = 64``` at the line ```out = awq_inference_engine.gemm_forward_cuda(x.reshape(-1, x.shape[-1]), self.qweight, self.scales, self.qzeroes, 8)``` in the ```linear.py``` file from the ```AutoAWQ``` package.