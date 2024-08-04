## https://huggingface.co/microsoft/table-transformer-detection/discussions/7

contains_question: yes

question_part: Can we do any preprocessing to obtain better detection results? In my case, I got full-page tables with alternating color rows (i.e. background for the first row is white, the second row is light yellow, the third is white again, and so on. The table transformer detector is not able to detect these tables. It works beautifully on regular tables that are homogenous in terms of background and are not full-page. I've tried  padding the corners of my images, but that doesn't work.