## https://huggingface.co/openbmb/cpm-bee-10b/discussions/3

contains_question: yes

question_part: Error type 2 - Using [the code](https://huggingface.co/openbmb/cpm-bee-10b/blob/main/modeling_cpmbee.py) in this huggingface repo with setting trust_remote_code=True

Modeling_cpmbee.py:787 in forward
│                                                                                                  │
│    784 │   │   │   │   + segment_rel_offset[:, :, None],                                         │
│    785 │   │   │   │   ~(                                                                        │
│    786 │   │   │   │   │   (sample_ids[:, :, None] == sample_ids[:, None, :])                    │
│ ❱  787 │   │   │   │   │   & (span[:, None, :] == span[:, :, None])                              │
│    788 │   │   │   │   ),  # not in the same span or sample                                      │
│    789 │   │   │   │   0,  # avoid torch.gather overflow                                         │
│    790 │   │   │   ).view(batch, seqlen * seqlen)                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
TypeError: 'NoneType' object is not subscriptable