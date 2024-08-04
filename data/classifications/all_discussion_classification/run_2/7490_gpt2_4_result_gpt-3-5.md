## https://huggingface.co/gpt2/discussions/4

contains_question: yes

question_part: When I train with text that has linebreaks because it came from PDF files, are they relevant for training? Currently I replace them with a space, as they are obviously learned and I think the net may generalize worse when it tries to interpret some semantic meaning into a linebreak, which isn't there. But maybe it also can learn that there is a linebreak every X chars, but that the linebreak does not have any meaning but wrapping lines to a readable length? What's common practice for data preprocessing? Does it matter for the text (not the formatting) if the net was trained on wrapped text?