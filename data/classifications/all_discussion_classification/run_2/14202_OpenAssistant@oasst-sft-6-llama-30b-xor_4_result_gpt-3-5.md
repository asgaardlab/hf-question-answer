## https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor/discussions/4

contains_question: yes

question_part: To convert the original llama 30B weights to HF format, it needs to fit the entire model into RAM (PC, not GPU VRAM, see https://huggingface.co/docs/transformers/main/model_doc/llama). That's more than 65GB of RAM. Chances are as a hobbyist you don't have that in your PC. If you: - run `python src/transformers/models/llama/convert_llama_weights_to_hf.py --input_dir /path/to/LLaMA --output_dir /path/to/converted_llama_hf --model_size 30B` - see your RAM go up to 100% in the activity monitor, - your PC freezes for a bit, - and then you see `killed` in the terminal.