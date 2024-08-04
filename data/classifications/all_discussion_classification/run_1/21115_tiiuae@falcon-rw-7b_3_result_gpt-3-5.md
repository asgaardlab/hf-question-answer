## https://huggingface.co/tiiuae/falcon-rw-7b/discussions/3

contains_question: yes

question_part: Here, Falcon has both concat dim = 1, but claims that key is (bs_times_num_head, head_dim, seq_len), while value is (bs_times_num_head, seq_len, head_dim). How does it work? Should both key and value shape be (bs_times_num_head, seq_len, head_dim) instead?