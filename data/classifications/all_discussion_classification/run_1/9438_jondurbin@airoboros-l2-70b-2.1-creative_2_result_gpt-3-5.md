## https://huggingface.co/jondurbin/airoboros-l2-70b-2.1-creative/discussions/2

contains_question: yes

question_part: 
1. What pre-prompt was given when training this model? (the string that wraps around the "instruction" and "response" values in the dataset)
- For example one of Alpaca's preprompts were defined as
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
{output}
```
Was the "instruction" value wrapped with "BEGIN INSTRUCTION", "END INSTRUCTION" before sending to .train()?
2. Do you recommend we contextualize the conversation between "USER:" and "ASSISTANT:"?
-  Based on line 4974 and 4614 of expert_createive.jsonl it looks like the turn template might do best if we prefance our character names with "USER: " and "ASSISTANT: "
- For instance on line 4614 of expert_createive.jsonl I see 
```
USER: Let's dive into the topic.
ASSISTANT: Nathaniel: Taking a moment to admire the...
```
- Meaning the turn template that might work best here would be something like:
`USER: <|user|> <|user-message|>\nASSISTANT: <|bot|> <|bot-message|>\n`
3. Would you recommend wrapping the character cards with "BEGINCONTEXT" and "ENDCONTEXT"?