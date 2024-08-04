## https://huggingface.co/hongyin/chat-goliath-120b-80k/discussions/2

contains_question: yes

question_part: 
1. Issues with Git LFS files during repository cloning:
- We attempted to clone the repository using the git clone command but faced issues with the Git LFS files. Each file was only 1KB in size and contained a description rather than the expected data.
``` [...] ```
- We then directly downloaded the files, ensuring their integrity through SHA256 checksums.

2. Strange Metadata and Incoherent Responses in Kobold.cpp:
- Upon loading the files with Kobold.cpp, we observed oddities in the metadata. The Q2_K parameter exhibited an irregular 3.37 BPW value, whose value should usually be around 2.625 BPW.
``` [...] ```
- The model's responses were also inconsistent and interspersed with a mix of Chinese and English, lacking coherence and relevance.
![...] ![...] ![...]

3. Quantization Attempt in exl2:
- However, the quantization process also failed to yield consistent replies, like the issues encountered in the previous steps.
![...]