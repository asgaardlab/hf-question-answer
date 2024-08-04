## https://huggingface.co/LLukas22/paraphrase-multilingual-mpnet-base-v2-embedding-all/discussions/1

contains_question: yes

question_part: Following pair is a 100% match, which is not unexpected: "Wer ist antragsberechtigt?" and "Wer ist antragsberechtigt?" 
But this similarity drops sub-70% by just adding 1 word: "Wer ist antragsberechtigt?" and "Wer ist antragsberechtigt? Test"
It drops even further with more appended 'Test' words. Is this expected behaviour?
Is this because of the asymmetric nature of the training Question -> Answer?