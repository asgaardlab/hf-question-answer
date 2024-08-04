## https://huggingface.co/Open-Orca/OpenOrca-Platypus2-13B/discussions/3

contains_question: yes

question_part: It seems a bit inconsistent with generating <|end_of_turn|> at the end of responses, sometimes I get "|<|end_of_turn|>" or "|end_of_turn]" etc, especially when asking about subjects that trigger the censoring, e.g. "where can I buy drugs?" I've copied the oobabooga settings from https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B but I don't know if I'm doing something wrong, it's a bug in text-generation-webui/llama.cpp, or if this is expected from this model.