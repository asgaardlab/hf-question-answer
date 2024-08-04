## https://huggingface.co/HuggingFaceM4/idefics-9b/discussions/12

contains_question: yes  
question_part: 
From my understanding, the `<fake_token_around_image>` replaces the `<EOC>` end of chunk token from the original Flamingo paper. According to the latter, the `<EOC>` token is used at the end of a text chunk: *"prior to any image and at the end of the document"*.  
Why this difference? Did you do or refer to experiments/ablation studies on this added token?