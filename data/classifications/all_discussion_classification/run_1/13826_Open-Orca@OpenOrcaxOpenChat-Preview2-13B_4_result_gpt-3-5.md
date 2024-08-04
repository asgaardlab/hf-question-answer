## https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B/discussions/4

contains_question: yes

question_part: The examples you give have `<|end_of_turn|>` as the only separator between user and assistant message, without any newlines:

`User: Hello<|end_of_turn|>Assistant: Hi<|end_of_turn|>User: How are you today?<|end_of_turn|>Assistant:`

But further down the page, your ooba prompt template has a newline after the separator and also after the assistant message:

`<|user|> <|user-message|><|end_of_turn|>\n<|bot|> <|bot-message|>\n`

So which is correct? And where, and how, is the "context" you give for ooba supposed to go in the prompt (I assume it's the system message)?