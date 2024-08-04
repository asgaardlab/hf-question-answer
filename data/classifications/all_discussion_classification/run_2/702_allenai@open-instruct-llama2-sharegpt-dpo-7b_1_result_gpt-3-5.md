## https://huggingface.co/allenai/open-instruct-llama2-sharegpt-dpo-7b/discussions/1

contains_question: yes

question_part: Hi !
I am trying to study some cases of success of DPO training and I tried your model:
```python
prompt = "How to load image here ?"
prompt = f"""<|user|>
{prompt}
<|assistant|>
"""
 
inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"].cuda()
generation_output = model.generate(
        input_ids=input_ids,
        return_dict_in_generate=True,
        output_scores=True,
        max_length=752,
        pad_token_id=tokenizer.eos_token_id
    )
for s in generation_output.sequences:
    output = tokenizer.decode(s)
    print(output)
```

I expected something like (https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized/viewer/default/train_prefs?p=2&row=212):

```
To load an image here, you can follow these simple steps:\n\n1. First, you need to upload the image to a file hosting or sharing service like Google Drive, Dropbox, or Imgur.\n\n2. Once the image is uploaded, get the image's URL (web address) from the hosting service.\n\n3. In your question or response, simply copy the image URL and paste it into the text box here. Be sure to select the \"image\" icon before doing so.\n\n4. After pasting the URL, the image will automatically appear within your question or answer.\n\nIf you need further assistance, please let me know.
```

But instead I got:

```
<s> <|user|>
How to load image here ?
<|assistant|>
To load an image in a Python script, you can use the `PIL` (Python Imaging Library) module. Here's an example of how to load an image using `PIL`:

from PIL import Image

# Load the image
image = Image.open("image.jpg")

# Display the image
image.show()

In this example, we first import the `Image` class from the `PIL` module. We then use the `Image.open()` method to load the image from the file "image.jpg". Finally, we display the image using the `show()` method.

Note that you need to install the `PIL` module before you can use it in your Python script. You can install it using pip:

pip install pillow

Also, make sure that the image file is in the same directory as your Python script or that you provide the full path to the image file in the `Image.open()` method.</s>

Did I do something wrong?

Thanks in advance !