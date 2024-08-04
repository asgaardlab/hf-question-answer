## https://huggingface.co/meta-llama/LlamaGuard-7b/discussions/11

contains_question: yes

question_part: 
1. Prompt Configuration: Could someone shed light on the ideal prompt used for the ToxiChat model? What kind of inputs or context tend to yield optimal results?
2. Dataset Handling: How is the ToxiChat dataset treated during inference? Any special preprocessing steps or considerations that contribute to the model's success?
3. Probability for "safe" and "unsafe": Could someone share insights on how to extract the probabilities associated with the predictions of the words "safe" and "unsafe" from the model's output? Right now, I obtain the logits of the words "safe" and "unsafe" and pass them through a softmax to obtain the probabilities that add up to 1.
4. Probability Thresholds for AUPRC: In calculating the AUPRC, which probability thresholds are used to determine positive and negative predictions?