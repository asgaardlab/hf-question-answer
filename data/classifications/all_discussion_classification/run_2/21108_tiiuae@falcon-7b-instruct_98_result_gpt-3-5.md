## https://huggingface.co/tiiuae/falcon-7b-instruct/discussions/98

contains_question: yes
question_part: So I am trying to do a QA app for a document and when I try to do this with ```qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())``` ```response = qa.run(query)```
When the llm is falcon-7b it responds in short(not complete response) and weird ways.