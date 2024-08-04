### Documents:
- SageMaker deploy failure - KeyError: 'gpt_neox'

I'm trying to run the sample code on SageMaker but the predictor fails:

from sagemaker.huggingface import HuggingFaceModel
import sagemaker

role = sagemaker.get_execution_role()
# Hub Model configuration. 
hub = {
	'HF_MODEL_ID':'EleutherAI/gpt-neox-20b',
	'HF_TASK':'text-generation'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.17.0',
	pytorch_version='1.10.2',
	py_version='py38',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge' # ec2 instance type
)

predictor.predict({
	'inputs': "Can you please let us know more details about your "
})

=====================

ModelError: An error occurred (ModelError) when calling the InvokeEndpoint operation: Received client error (400) from primary with message "{
  "code": 400,
  "type": "InternalServerException",
  "message": "\u0027gpt_neox\u0027"
}

The corresponding logs:
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle -     config = AutoConfig.from_pretrained(model, revision=revision, _from_pipeline=task, **model_kwargs)
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle -   File "/opt/conda/lib/python3.8/site-packages/transformers/models/auto/configuration_auto.py", line 657, in from_pretrained
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle -     config_class = CONFIG_MAPPING[config_dict["model_type"]]
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle -   File "/opt/conda/lib/python3.8/site-packages/transformers/models/auto/configuration_auto.py", line 372, in __getitem__
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle -     raise KeyError(key)
W-EleutherAI__gpt-neox-20b-1-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle - KeyError: 'gpt_neox'

Any idea how to solve it?
- Not able to deploy on AWS Sagemaker

I am a newbie and trying to deploy this model on Sagemaker so that I can get some endpoint to use for text generation. I get 400 error from the backend. Can anyone help?
- Deployment error on Sagemaker: could not load model

Hi,
I'm trying to deploy an endpoint for of this model using sagemaker, specifically the code offered under 'Deploy':

import sagemaker
import boto3
from sagemaker.huggingface import HuggingFaceModel

try:
	role = sagemaker.get_execution_role()
except ValueError:
	iam = boto3.client('iam')
	role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

# Hub Model configuration. 
hub = {
	'HF_MODEL_ID':'microsoft/BioGPT-Large-PubMedQA',
	'HF_TASK':'text-generation'
}

# create Hugging Face Model Class
huggingface_model = HuggingFaceModel(
	transformers_version='4.26.0',
	pytorch_version='1.13.1',
	py_version='py39',
	env=hub,
	role=role, 
)

# deploy model to SageMaker Inference
predictor = huggingface_model.deploy(
	initial_instance_count=1, # number of instances
	instance_type='ml.m5.xlarge' # ec2 instance type
)

predictor.predict({
	"inputs": "Can you please let us know more details about your ",
})

The deployment succeeded, but when calling predict, the workers die because they cannot load the model. When looking at the Cloudwatch logs, I see the following error: 

2023-07-25T14:48:59,331 [INFO ] W-9000-microsoft__BioGPT-Large-P-stdout com.amazonaws.ml.mms.wlm.WorkerLifeCycle - ValueError: Could not load model /.sagemaker/mms/models/microsoft__BioGPT-Large-PubMedQA with any of the following classes: (<class 'transformers.models.auto.modeling_auto.AutoModelForCausalLM'>, <class 'transformers.models.biogpt.modeling_biogpt.BioGptForCausalLM'>).

Any idea on how to solve? Perhaps I need to use a newer version of transformers?
### Keywords: sagemaker, deploy, endpoint, aws, error, tgi, inference, aws sagemaker, instance, ml