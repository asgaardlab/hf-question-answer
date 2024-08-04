### Documents:
- Inference speed

Great work! How fast is the inference? They say QLora is slow at inference, is it true?
- Inference speed is slow

I am trying to load this model for inference on a databricks notebook using the code provided in model card. But I am having a very low inference speed. It takes around 40-50 seconds to provide the answer even for simple prompts. How can I speedup this inference time?

My databricks cuda version is 11.4 .
- Mac m1 runs painfully slow

I wrote a script to make an inference on an audio file, and it took 30 minutes to get a response:

script:

`
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

Initialize model
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen-Audio-Chat", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen-Audio-Chat", device_map="cpu", trust_remote_code=True).eval()

Set up audio file
audio_file = "file.mp3"

Define helper validation function
def validate_response(text):
if ',' not in text:
print("Error - response did not contain comma delimited list")
return False
return True

Time full execution
start = time.time()

Attempt audio analysis
try:
query = tokenizer.from_list_format([
{'audio': audio_file},
{'text': 'Describe this audio with 5 comma-separated adjectives'},
])
response, history = model.chat(tokenizer, query=query, history=None)

# Print full response and validate
print(response)
valid = validate_response(response)
except Exception as e:
print(f"Error: {e}")
valid = False

end = time.time()
elapsed = end - start

Print total time
print(f"Elapsed time: {elapsed} seconds")

Check if the response was valid
if not valid:
print("Issues with audio analysis")`

result:

`python caption_audio.py
audio_start_id: 155164, audio_end_id: 155165, audio_pad_id: 151851.
Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency 
Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency 
Warning: import flash_attn fail, please install FlashAttention to get higher efficiency 
Loading checkpoint shards: 100%|██████████████| 9/9 [00:00<00:00, 17.97it/s]
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Audio 1:file.mp3
Describe this audio with 5 comma-separated adjectives<|im_end|>
<|im_start|>assistant

Funky, groovy, energetic, hip-hop, dance
Elapsed time: 1812.089405298233 seconds`

Also inconsistent results running the same script a subsequent time:

second result:

`python caption_audio.py
audio_start_id: 155164, audio_end_id: 155165, audio_pad_id: 151851.
Warning: import flash_attn rotary fail, please install FlashAttention rotary to get higher efficiency 
Warning: import flash_attn rms_norm fail, please install FlashAttention layer_norm to get higher efficiency 
Warning: import flash_attn fail, please install FlashAttention to get higher efficiency 
Loading checkpoint shards: 100%|██████████████| 9/9 [00:00<00:00, 9.99it/s]
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Audio 1:file.mp3
Describe this audio with 5 comma-separated adjectives<|im_end|>
<|im_start|>assistant

This is a funky, groovy, upbeat, electronic, electro, electronic beats, electronic music, electronic dance, electronic instrumental, electronic background, electronic soundtrack, electronic soundtrack, electro hip hop, electro hip hop beats, electro hip hop instrumental, electro rap, electro rap beats, electro rap instrumental, electronic music for tv, electronic music for radio, electronic music for advertising, electronic music for games, electronic music for movies, electronic music for youtube, electronic music for corporate use, electronic music for commercial use, electronic music for business, electronic music for presentations, electronic music for websites, electronic music for apps, electronic music for software, electronic music for advertising, electronic music for marketing, electronic music for product presentation, electronic music for corporate presentations, electronic music for business videos, electronic music for product videos, electronic music for commercials, electronic music for radio, electronic music for tv, electronic music for films, electronic music for viral marketing, electronic music for web advertisements, electronic music for youtube videos, electronic music for social media, electronic music for apps, electronic music for mobile, electronic music for corporate, electronic music for background, electronic music for fashion, electronic music for lifestyle, electronic music for beauty, electronic music for food, electronic music for travel, electronic music for health, electronic music for fitness, electronic music for meditation, electronic music for relaxation, electronic music for studying, electronic music for working, electronic music for sleeping, electronic music for dancing, electronic music for fun, electronic music for playing, electronic music for singing, electronic music for podcast, electronic music for video games, electronic music for background music, electronic music for club, electronic music for rapping, electronic music for beat-making, electronic music for producing, electronic music for composing, electronic music for singing, electronic music for playing, electronic music for dancing, electronic music for fun, electronic music for playing, electronic music for singing, electronic music for producing, electronic music for composing, electronic music for radio, electronic music for tv, electronic music for films, electronic music for viral marketing, electronic music for web advertisements, electronic music for youtube videos, electronic music for social media, electronic music for apps, electronic music for mobile, electronic music for corporate, electronic music for background, electronic music for fashion, electronic music for lifestyle, electronic music for beauty, electronic music for food, electronic music for travel, electronic music for health, electronic music for fitness, electronic music for meditation, electronic music for relaxation, electronic music for studying, electronic music for working, electronic music for sleeping, electronic music for
Elapsed time: 60488.493457078934 seconds`

any tips to make this run more efficiently?
### Keywords: electronic, music, inference, speed, time, td, slow, faster, inference time, inference speed