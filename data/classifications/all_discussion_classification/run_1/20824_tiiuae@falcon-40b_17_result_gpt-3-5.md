## https://huggingface.co/tiiuae/falcon-40b/discussions/17

contains_question: yes
question_part: After reading your RW paper, I got a question regarding your choice of positional encodings. In your paper, ALiBi was used to train RW-1B/7B. However, your ultimate models (falcon-7B/40B) were using rotary. According to the ALiBi and XPos papers, ALiBi outperforms rotary much, especially when applied to context longer than the pretrain limit. So, could you explain why you revert ALiBi to rotary in your final large-scale pretraining