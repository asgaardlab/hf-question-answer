## https://huggingface.co/Minami-su/Yi_34B_Chat_2bit/discussions/1

contains_question: yes

question_part: Hi, I saw that you quantized Yi 34B with QuIP#, exciting to see our stuff being used. I was playing around with this model on interactive_gen.py and it doesn't seem to be very good at handling chinese tokens. Did you generate hessians with the default redpajama dataset we hardcoded in hessian_offline_llama.py? If so, you'll want to generate hessians with a chinese + english dataset to get accurate hessians for quantization.