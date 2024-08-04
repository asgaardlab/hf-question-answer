## https://huggingface.co/bigscience/bloom-7b1/discussions/49

contains_question: yes

question_part: I wanted to know the correct prompt formatting for `bloom-7b1`.  I have tried some of the prompts : Eg: import time start = time.time() query="""Given a question delimitted by triplebackticks. \nUser: ```के आफूले मन पराएको व्यक्तिले राखेको यौन सम्पर्कको मागलाई स्वीकार्नु ठीक हो ?```\nAssistant:""" inputs = tokenizer.encode(query , return_tensors="pt").to("cuda") outputs = model.generate(inputs , max_new_tokens = 200 , temperature = 0.5, do_sample=True) ans = tokenizer.batch_decode(outputs , skip_special_tokens = True)[0] print( ans[len(query):]) print("inferecne time",  time.time() - start) The answer extremely hallucinates.  What can be done?