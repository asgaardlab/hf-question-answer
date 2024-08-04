## https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF/discussions/3

contains_question: yes
question_part: The current command is `huggingface-cli download TheBloke/Phind-CodeLlama-34B-v2-GGUF phind-codellama-34b-v2.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False`. This is incorrect and will lead to an `Entry Not Found for url` error. The correct command is `huggingface-cli download TheBloke/Phind-CodeLlama-34B-v2-GGUF phind-codellama-34b-v2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False`. Notice the capitalized Q.