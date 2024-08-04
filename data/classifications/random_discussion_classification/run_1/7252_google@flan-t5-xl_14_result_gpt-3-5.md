## https://huggingface.co/google/flan-t5-xl/discussions/14

contains_question: yes
question_part: 
1. currently, I'm use my data(20 files) to create embedding from HuggingFaceEmbeddings. Even if I have 2 millions files do I need to follow the same steps like 1.create embedding from HuggingFaceEmbeddings, 2. do similarity test, and 3. pass it to model?
2. At what stage I need to retrain the LLM?
3. is it possible to retrain the LLM with my own data? or is there a concept "retraining" in LLM?
4. currently, I'm using chromadb as vector db, In case if I want to move it production how do I host it? where do I store all my data(embeddings)? 
5. do  I need to store all embedding in any database, if yes, could you please recommend any?
6. how do I evaluated "google/flan-t5-xl" LLM with my data?
7. currently, I noticed "google/flan-t5-xl" model with my data gives one wrong answer. so, how do I correct the model? if it is other model like text classification I would correct the label and retrain the model with corrected label. how do I do it here?
8. how to do I get same answer whenever I run the model? like reproducibility having torch.manual_seed(0), should I mention this to get reproducibility?