## https://huggingface.co/hongyin/chat-goliath-120b-80k/discussions/2

contains_question: yes

question_part: 
1. Issues with Git LFS files during repository cloning:
- We attempted to clone the repository using the git clone command but faced issues with the Git LFS files. Each file was only 1KB in size and contained a description rather than the expected data.
2. Strange Metadata and Incoherent Responses in Kobold.cpp:
- Upon loading the files with Kobold.cpp, we observed oddities in the metadata. The Q2_K parameter exhibited an irregular 3.37 BPW value, whose value should usually be around 2.625 BPW.
3. Quantization Attempt in exl2:
- Moving forward, we attempted to quantize the model in exl2. We first converted the model into .safetensors, with our SHA256 for the .safetensors matching the expected values.