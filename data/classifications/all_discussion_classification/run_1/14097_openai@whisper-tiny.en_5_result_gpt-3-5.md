## https://huggingface.co/openai/whisper-tiny.en/discussions/5

contains_question: yes

question_part: When i use the example 
```{Python}
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset
import torch

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

# load dummy dataset and read soundfiles
ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
input_features = processor(ds[0]["audio"]["array"], return_tensors="pt").input_features 

# Generate logits
logits = model(input_features, decoder_input_ids = torch.tensor([[50258]])).logits 
# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
```

I get result `['<|startoftranscript|>']`

However, if I do
```{Python}
generated_ids = model.generate(inputs=input_features)
transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(transcription)
```

I get result ` Mr. Quilter is the apostle of the middle classes, and we are glad to welcome his gospel.`