## https://huggingface.co/ramadita/ID-Llama-2-7b-Chat-GPTQ/discussions/1

contains_question: yes
question_part: I see you have liked Photolens/llama-2-7b-langchain-chat model and I wondered is your model here is cloned from his'? I as because I tried to use his model but with a standard prompt template, I got terrible answers and I assume there is some change in the template for chat. For example, my prompt template looks like this:          [INST]<\<SYS\>\>
        You are a helpful assistant, etc.
        <\<\/SYS\>\>

        Context: {context}
        User: {question}

        [/INST]

It works perfectly with TheBloke's model but with this one, I get results formatted like this:
```json
{"action": "Final Answer", "action_input": <text>}
```  січня 18, 2023, 15:45 (UTC)

<INST> <text>[/INST] 
```json
{"action": "Final Answer", "action_input": <text>}
```  janvier 18, 2023, 15:47 (UTC)

<INST> <text>}
```  enero 18, 2023, 15:47 (UTC)

<INST> <text> [/INST] ```json
{"action": "Final Answer", "action_input": <text>}
```  janvier 18, 2023, 15:47 (UTC)
...
```