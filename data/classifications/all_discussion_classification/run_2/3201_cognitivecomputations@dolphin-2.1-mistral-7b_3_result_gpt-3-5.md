## https://huggingface.co/cognitivecomputations/dolphin-2.1-mistral-7b/discussions/3

contains_question: yes

question_part: As per the original Orca paper, the training for their model used GPT-3.5 completions as an intermediary target to meet before later training on GPT-4 completions, making sure the model has been *finalized* with the higher quality data (from GPT-4) at its training completion. Relevant excerpt from paper:
> We first train Orca on FLAN-5M (ChatGPT augmentations), followed by second stage of training on FLAN-1M (GPT-4 augmentations). Essentially, we leverage ChatGPT as intermediate teacher assistant for two reasons.<br/><br/>• Capacity gap: Orca with 13B parameters is many times smaller than GPT-4 (size undisclosed). Leveraging an intermediate teacher with reduced gap in capabilities, in this case ChatGPT, has been shown to improve imitation learning performance for smaller students in knowledge distillation [15]. This can be viewed as a form of progressive learning or curriculum learning, where the student first learns from easier examples, followed by harder ones: with the assumption that longer responses are difficult to mimic than shorter ones, along with improved reasoning and step-by-step explanation from a larger teacher . . .

If this is the case, future training could benefit from a more ordered learning process, for instance: 3 epochs of GPT-3.5 completions (w. shuffling on each epoch and a suitable LR scheduler) -> 5 epochs of GPT-4 completions, where `airoboros` data (which is from GPT-4) could be mixed into.

The other question is on the filtering for both GPT completions: was the deduplication step in filtering performed per-set or across both GPT-4 and GPT-3.5 sets? Deduplication should have been performed per-set with GPT-3.5 and GPT-4 completions treated as completely separate datasets, given the curriculum learning intentions.

Last is a small question about the formatting. It seems the model outputs for the assistant role always begin with a token containing a space character (logged from llama.cpp, notice token 6880):