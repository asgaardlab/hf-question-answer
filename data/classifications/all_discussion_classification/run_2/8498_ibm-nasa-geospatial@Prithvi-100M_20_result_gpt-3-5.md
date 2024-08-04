## https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M/discussions/20

contains_question: yes

question_part: 
1. Size of the training dataset in terms of the number of images used for MAE pre-training. Is this a curated version of HLS Landsat? or were all the images available used?
2. What is the time period/interval between time stamps provided to the model during training? What is the reasoning behind this choice and does the choice of the time stamp (during inference) impact the performance?
3. Was the MAE masking percentage 75%? and for how many epochs were they trained?
4. Why [B, C, T, H, W] and not [B, T*C, H, W]?
5. In order to train the model, were all the tiles from Continental US used or specific regions within CONUS?
6. Quality of MAE reconstruction in terms of SSIM? I did try using the model for certain patches in the US and the reconstruction quality was around 0.8 ish with patching artefacts.