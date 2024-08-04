## https://huggingface.co/TheBloke/tulu-30B-GGML/discussions/1

contains_question: yes

question_part: It performs very well in my tests, which is an execution of the chain: "(loop (-> get-task-description llm_generate_plan llm_convert_plan_to_json parse_command))" and what I measure is the number of steps to first command which leads to meaningful results.