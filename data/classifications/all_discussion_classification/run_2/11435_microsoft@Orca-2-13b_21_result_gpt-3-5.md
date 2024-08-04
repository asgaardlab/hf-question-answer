## https://huggingface.co/microsoft/Orca-2-13b/discussions/21

contains_question: yes

question_part: 
I tripped over what seems to be built in support for reading and summarizing documents while trying to write a script to load PDFs and answer questions about them.
It's either not really supported and is just the model generating odd text or I am not using it right.
My script builds a prompt using the system prompt from this model page with my prompt appended then passes that to the model.
I'm suspicious because the model responses have nothing to do with the document content.
The session transcript follows, where 'Orca2>' is my command prompt that I enter text at.