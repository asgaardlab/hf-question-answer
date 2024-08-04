## https://huggingface.co/ydshieh/kosmos-2-patch14-224/discussions/14

contains_question: yes

question_part: By default, your model always inserts an image at the beginning of the input text. However, I wanted to use text interleaved with an image as an input, such as "This image {image comes here} is ...". So I made a wrapper class for the processor to accept an image in an arbitrary position in the text. Here's the code. When using this wrapped processor, you can use `<image>` to specify the location of the image in the input text.
I tried this, and it seemed to work (it can't accept bounding boxes, though). Do you think this wrapper is reasonable and works fine?
Also, I want to insert multiple images in the input, but I haven't figured out how. Do you have any plans to release codes for multiple images?