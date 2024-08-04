## https://huggingface.co/microsoft/phi-2/discussions/55

contains_question: yes
question_part: Q1:
pipe("say hello to my little friend", max_length=100)
[{'generated_text': 'say hello to my little friend"\n    """\n    return f"{name}, {name}, bo-b{name}, banana-fana fo-f{name}, fee-fi-mo-m{name}, {name}!"\n\n\n\nfrom typing: List\n\ndef average_of_all_odds(li: List[int]) -> float:\n    """\n    Given a list of integers, returns the average of all the odd integers in'}]

Q2
pipe("i can fly. 5 possibilities for the scenerio in which it was said are:", max_length=100)
[{'generated_text': 'i can fly. 5 possibilities for the scenerio in which it was said are:\n\n1. The bird is a bird that can fly.\n2. The bird is a bird that cannot fly.\n3. The bird is a bird that can fly, but it is not a bird that can fly.\n4. The bird is a bird that cannot fly, but it is a bird that can fly.\n5. The bird is a bird that cannot fly, but it'}]