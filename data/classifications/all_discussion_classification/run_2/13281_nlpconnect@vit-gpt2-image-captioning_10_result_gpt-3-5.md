## https://huggingface.co/nlpconnect/vit-gpt2-image-captioning/discussions/10

contains_question: yes

question_part: 
- I am facing an issue in creating a Hosted Inference API , as the pipeline gives an error of "Unidentified feature_extractor" while building the pipeline. So to fix this issue I manually made changes in `preprocessor_config.json` as it was containing <b>"image_processor_type": "ViTImageProcessor" </b>.
I crosschecked with your file and it shows <b>"feature_extractor": "ViTFeatureExtractor" </b>. 

- Another issue is if I manually change the file and the pipeline is built then while calling the pipeline  <b>`"captioner("image.jpg")"`</b> , it throws an error saying `preprocess_fn() got an unexpected keyword argument 'images'`