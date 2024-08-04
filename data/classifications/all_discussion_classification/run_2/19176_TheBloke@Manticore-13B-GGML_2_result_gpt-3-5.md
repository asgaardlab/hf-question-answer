## https://huggingface.co/TheBloke/Manticore-13B-GGML/discussions/2

contains_question: yes

question_part: Although on some questions it just goes ballistic and won't stop. It keeps repeating the answer, just differently each time, but unless I CTRL+C out, it would keep going until the world ends.

Also, is there a way to run in llama.cpp interactive mode (for example with Wizard-Mega model it was pretty neat as it remembered the prior conversation) ?

I tried with --interactive-first and using -r "user " as a prompt for it to stop, but it only works the first time. After that it keeps repeating the "user" with some random question (though it does not answer it). Plain -i(nteractive) does not work and it just takes off here writing code in various languages. It's amusing but not useful. :)

I also noticed that if I ask the same question in the --ins(truction) mode it gives me a different (and apparently longer) answer than with the --interactive-first mode.