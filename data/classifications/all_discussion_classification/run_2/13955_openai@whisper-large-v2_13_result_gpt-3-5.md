## https://huggingface.co/openai/whisper-large-v2/discussions/13

contains_question: yes

question_part: Unfortunately, it seems like the results from the HF inference endpoint are significantly worse than the local results (though they both use the `large-v2` model). About ~30% of the transcription / audio is "missing". Certain "chunks" of the transcription are just not there (like sections of say 20 seconds or so of audio do not get transcribed). Any tips or tricks to help debug why this may be happening?