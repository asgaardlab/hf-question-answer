## https://huggingface.co/nomic-ai/gpt4all-mpt/discussions/2

contains_question: yes

question_part: By the way, this model also doesn't support the optimized triton implementation of FlashAttention like `mosaicml/mpt-7b-instruct`. If you turn it on via `config.attn_config['attn_impl'] = 'triton'`, you will get the same `KeyError: 'transformer.blocks.11.ffn.down_proj.weight'` error.