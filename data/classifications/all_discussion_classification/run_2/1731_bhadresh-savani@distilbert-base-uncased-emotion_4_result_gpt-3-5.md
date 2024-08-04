## https://huggingface.co/bhadresh-savani/distilbert-base-uncased-emotion/discussions/4

contains_question: yes

question_part: This model is interesting, but there is one significant issue: it does not have a neutral label. I'm processing a business email dataset - just the Subject lines for now - and there are a lot of strings there that do not exhibit any emotion, just regular business terms. Yet the model assigns them all kinds of emotions. Also, simply feeding an empty string to the model makes it assign emotions to it. I think the model would become much more useful if it also had a neutral output that was assigned properly when the text was indeed neutral.