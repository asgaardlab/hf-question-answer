## https://huggingface.co/mistralai/Mistral-7B-v0.1/discussions/65

contains_question: yes

question_part: When I try to use Mistral with the following parameters: --fsdp 'full_shard auto_wrap' --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' It reports error: Exception: Could not find the transformer layer class to wrap in the model.