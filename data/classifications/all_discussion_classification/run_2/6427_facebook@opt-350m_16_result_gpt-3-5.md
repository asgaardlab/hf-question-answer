## https://huggingface.co/facebook/opt-350m/discussions/16

contains_question: yes

question_part: What I'm trying to do is download the files directly from this page and then run opt locally. I notice the file structure here does not match the file structure when I run opt-350m on collab, which distributes files in root/.cache/huggingface/hub among several different folders. 

It isn't clear to me if I can manually distribute the files appropriately, or if the file structure will be constructed when running pipeline (but then where do I put the files so they are detected?)

Basically, if I download these files directly, where do I put it so that the hugging face transformers library can detect and use it.