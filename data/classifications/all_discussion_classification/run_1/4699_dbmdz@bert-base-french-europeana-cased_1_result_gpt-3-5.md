## https://huggingface.co/dbmdz/bert-base-french-europeana-cased/discussions/1

contains_question: yes
question_part: I tried to run locally the python code provided on the main page but I get a error:
```python
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-french-europeana-cased")
model = AutoModel.from_pretrained("dbmdz/bert-base-french-europeana-cased")
```

```OSError: dbmdz/bert-base-french-europeana-cased does not appear to have a file named config.json. Checkout 'https://huggingface.co/dbmdz/bert-base-french-europeana-cased/None' for available files.```

Is it normal ? Do I have to DL the model ?