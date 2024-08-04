## https://huggingface.co/oliverguhr/german-sentiment-bert/discussions/4

contains_question: yes
question_part: A quick note about applying this to larger dataframes, so if I pass in a larger (10,000 and above) items to `SentimentModel.predict_sentiment()` my process (terminal) usually freezes and then gets terminated by the OS. Next I tried `pandas.DataFrame.apply(...)` to add it row-wise, which I ended up closing after 5 hours. What ultimately ended up working for me is chunking the dataframe with `numpy.array_split` into chunks and wrapping a generator around it to yield the sentiment as chunks and then concatenating the result. Is there a better/more elegant way to do this?