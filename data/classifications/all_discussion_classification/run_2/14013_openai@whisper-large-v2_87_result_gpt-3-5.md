## https://huggingface.co/openai/whisper-large-v2/discussions/87

contains_question: yes

question_part: 
1 - I believe that I need to use an HF pipeline in order to leverage the "chunking" feature.  I need to transcribe files that are much longer than 30 secs, so believe that the pipeline is the only way to use chunking.  I was able to successfully create a torchserve mar file (model archive); however, I can't find a way to create a pipeline utilizing the model saved in the mar file.

2 - If it's not possible to create the pipeline from the resources in the mar file, can I just create it using:

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large-v2",
  chunk_length_s=30,
  device=device,
)

and place the above code in the Torchserve custom handler's initialization function?  If I have a local copy of the pytorch_model.bin, is there a way to just load that into a model object that can be passed as the model parameter into the pipeline constuctor?  Seems like I'd need to somehow set up the processor/tokenizer as well.

I have no specific loyalty to Torchserve, but need some way to robustly serve this model.  Seems like solid approach, but if there's something else that anyone would recommend, I'm open.

Thanks for any suggestions.