## https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B/discussions/13

contains_question: yes

question_part: I believe you trained using axolotl with this dataset config:
```
datasets:
  - path: /data/chat_data/full_dataset_chat.jsonl
    type: sharegpt
    conversation: chatml
dataset_prepared_path: last_run_prepared
```
Did you realised that Axolotl actually adds an extra linebreak (somehow) and it becomes `