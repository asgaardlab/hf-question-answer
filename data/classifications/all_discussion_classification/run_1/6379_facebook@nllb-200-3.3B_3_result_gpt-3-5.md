## https://huggingface.co/facebook/nllb-200-3.3B/discussions/3

contains_question: yes

question_part: When translating longer texts (multiple sentences), quite often it translates 1-2 sentences before starting to repeat itself (either a specific word or a sentence) until max_length is reached. Characters like | or & seems to trigger this behavior sometimes, but sometimes this happens without any such characters present. Email addresses seems to be a problem too, with "jean@medecin.fr" becoming "The following information is provided for each Member State:" when translating from French to English. I'm just wondering if anyone else have experienced something similar? Haven't seen these problems with M2M100, for example.