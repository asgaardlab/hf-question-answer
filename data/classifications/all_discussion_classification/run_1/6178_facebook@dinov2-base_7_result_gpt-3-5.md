## https://huggingface.co/facebook/dinov2-base/discussions/7

contains_question: yes

question_part: I noticed that the image preprocessor is configured to resize the image such that the shortest edge is 256 pixels, but then crop the image to 224x224. Is this deliberate? In other words, is it intended that part of the image will always be cut off even along the shortest edge