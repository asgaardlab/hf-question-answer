### Documents:
- The ONNX model is misaligned with the torch model

Hey, thansk for the great open source. I got stuck in the onnx model and could you help me out ? 
I exported  the onnx model by this command:"python3 -m transformers.onnx --model='sentence-transformers/all-MiniLM-L6-v2". 
I tested the onnx model using the following codes:

And I got the results:


Meanwhile, I encoded the same sentences using torch 

And the results were the folloiwngs, which were not aligned with onnx model's

I have checked the ouputs of the tokenizer and they all are the same. 
So is there anything wrong with my onnx codes or the onnx model itself ?
- Model Export to ONNX format

Is there any pipeline to export this model to ONNX (using torch.onnx/optimum, etc)? I intend to do further acceleration in inference and ONNX file is a must. However, none of the frameworks above support baichuan yet.
- Onnx export failed on trust_remote_code

I tried loading the model's Onnx:



Can you add a Onnx-version in the repo directly?
### Keywords: onnx, onnx model, model onnx, export, convert, onnx version, onnxruntime, model, js, optimum