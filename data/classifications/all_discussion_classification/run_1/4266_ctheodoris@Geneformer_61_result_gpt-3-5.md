## https://huggingface.co/ctheodoris/Geneformer/discussions/61

contains_question: yes
question_part: I noticed that the provided "example_lengths_file" is recommended to be passed as argument `example_lengths_file` in `GeneformerPretrainer`, however the lengths in it are sorted. While in `CustomDistributedLengthGroupedSampler`, the lengths should be the length the same order in `genecorpus_30M_2048.dataset`instead of being sorted. Could you help to clarify this?