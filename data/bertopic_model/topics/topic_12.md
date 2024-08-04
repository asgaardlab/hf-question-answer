### Documents:
- Short form transcription - Does distil-medium.en only transcribe for max 30 seconds of a video/audio?

Hi,

I am just testing this new model. I used openai's whisper for transcribing an audio (~ 4 mins length) and it transcribes the whole audio.

I used short form transcription using distil-medium.en using the code shown on the model card page but it only transcribes the first 30 seconds. Why is that so?

Here's the code:

import os
import argparse
import whisper
import time
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from writeToJSON import createJSON

def openai_transcript(vid_path):
    model = whisper.load_model('medium.en', device = "cpu")
    print(f"Transcribing {vid_path} using openai whisper...")
    start_time = time.time()
    result = model.transcribe(vid_path)
    end_time = time.time()
    return result["text"], f"{end_time - start_time:.2f} seconds"
    # print(f"{vid_path} using openai whisper took => {end_time - start_time:.2f} seconds")

def distil_whisper_transcript(vid_path):
    device = "cpu"
    torch_dtype = torch.float32
    model_id = "distil-whisper/distil-medium.en"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, use_safetensors=True #low_cpu_mem_usage=True,
    )
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        # max_new_tokens=128,
        torch_dtype=torch_dtype,
        device=device,
    )
    print(f"Transcribing {vid_path} using distil-whisper...")
    start_time = time.time()
    result = pipe(vid_path)
    end_time = time.time()
    return result["text"], f"{end_time - start_time:.2f} seconds"
    # print(f"{vid_path} using distil-whisper took => {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Transcription-summarization pipeline")

    # Define expected command-line arguments
    parser.add_argument('--vid_folder', type=str, help='Enter the video file path')
    # Parse the command-line arguments
    args = parser.parse_args()
    vid_folder = args.vid_folder

    for vid in os.listdir(vid_folder):
        vid_path = os.path.join(vid_folder, vid)
        # Transcribe using openai whisper medium.en
        transcript_openai, time_openai = openai_transcript(vid_path)
        # Transcribe using distil-whisper medium.en
        transcript_distil, time_distil = distil_whisper_transcript(vid_path)
        createJSON(vid_path, transcript_openai, time_openai, transcript_distil, time_distil, "output.json")
- Performance degradation on known langauges of whisper

I was trying to do a chat over a audio. Whisper-v2 audio output transcription was good like near perfect but the transcrition output of qwen did not capture whole transcription. I was trying it on hindi audio assuming whisper performance for hindi very good. Next i tried summarising audio but that also did not give proper results. Anyone who has tried qwen for languages supported by whisper?
- How can I detect the language of the audio by loading the model named WhisperForConditionalGeneration? 

# This is how I expect to load the model
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")

# This is the language detection method mentioned in the README of whisper
import whisper
model = whisper.load_model("base")
audio = whisper.load_audio("audio.mp3")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")
### Keywords: audio, whisper, transcription, speech, transcribe, voice, language, file, output, model