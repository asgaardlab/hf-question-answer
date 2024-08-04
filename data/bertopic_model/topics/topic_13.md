### Documents:
- Performing MLM pretraining on BERT pretrained model to use model in Sentence Transformer for semantic similarity

I have a NLP use case to compute semantic similarity between sentences that are very specific to my use case.  
I want to use [Sentence Transformers][1] library to do this, which provides with state of the art result for this goal.  

I have a BERT model specifically trained for the sBERT task and I know I can finetune the model with pair of sentences as inputs and similarity score as labels.  
However, I would also like to continue BERT pretraining with Mask Language Modeling task on this model.  
Does it make sense to instantiate a BertForMaskedLM object from this model already trained for sentence transformer task in order to continue its pretraining, and then load it as a SentenceTransformer model to finetune it on sentence pairs? 

I would do as such, with example on [Camembert French NLP model from huggingface][2] :

For the MLM part:


To get it as SentenceTransformer model:


Thanks ! 

  [1]: 
  [2]:
- How do I pass a Vector database into a Dolly LLM?

So here is my other question. If you were to work from OpenAI to LangChain. We take a given document and put it in a vector database and then you persist your Chroma vector store like so:

from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

from langchain.vectorstores import Chroma
persist_directory = "vector_db"
vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_directory)

vectordb.persist()
vectordb = None
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)
doc_retriever = vectordb.as_retriever()

from langchain.chains import RetrievalQA
resume_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=doc_retriever)

As you can see here the "vectordb" retriever is stored in "doc_retriever". This is very simple. At this point you can run any query based off the documentation you uploaded. Now I am trying to do this with Dolly.

Now here is my code:
loader = PyPDFLoader("/content/drive/MyDrive/Data Science/Capstone/Resume_guide.pdf")
pages = loader.load_and_split()

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-7b")

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
chunk_size = 1000,
chunk_overlap = 20,
length_function = len,
)

documents = text_splitter.split_documents(pages)
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import Chroma

persist_directory = "vector_db"
vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_directory)

vectordb.persist()
vectordb = None

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

doc_retriever = vectordb.as_retriever()

#Dolly Stuff
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
from transformers import pipeline

generate_text = pipeline(model="databricks/dolly-v2-7b", torch_dtype=torch.bfloat16,
trust_remote_code=True, device_map="auto", return_full_text=True)

#Dolly Stuff
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline

#template for an instruction with no input
prompt = PromptTemplate(
input_variables=["instruction"],
template="{instruction}")

#template for an instruction with input
prompt_with_context = PromptTemplate(
input_variables=["instruction", "context"],
template="{instruction}\n\nInput:\n{context}")

hf_pipeline = HuggingFacePipeline(pipeline=generate_text)

llm_chain = LLMChain(llm=hf_pipeline, prompt=prompt)
llm_context_chain = LLMChain(llm=hf_pipeline, prompt=prompt_with_context)

What I don't understand is how will "doc_retriever" be used in the llm_context_chain or llm_chain variables?

I noticed no where in my code, I am not calling "doc_retriever". How would I do that? Is there any documentation for uploading your own documentation in Dolly while using HuggingFace? Any help would be greatly appreciated!
- How to use your own data with Dolly

So here is my other question. If you were to work from OpenAI to LangChain. We take a given document and put it in a vector database and then you persist your Chroma vector store like so:

from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

from langchain.vectorstores import Chroma
persist_directory = "vector_db"
vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_directory)

vectordb.persist()
vectordb = None
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0)
doc_retriever = vectordb.as_retriever()

from langchain.chains import RetrievalQA
resume_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=doc_retriever)

As you can see here the "vectordb" retriever is stored in "doc_retriever". This is very simple. At this point you can run any query based off the documentation you uploaded. Now I am trying to do this with Dolly. 



Now here is my code:
loader = PyPDFLoader("/content/drive/MyDrive/Data Science/Capstone/Resume_guide.pdf")
pages = loader.load_and_split()

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-7b")

from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 20,
    length_function = len,
)

documents = text_splitter.split_documents(pages)
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import Chroma

persist_directory = "vector_db"
vectordb = Chroma.from_documents(documents=documents, embedding=embeddings, persist_directory=persist_directory)

vectordb.persist()
vectordb = None

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

doc_retriever = vectordb.as_retriever()

#Dolly Stuff
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
from transformers import pipeline

generate_text = pipeline(model="databricks/dolly-v2-7b", torch_dtype=torch.bfloat16,
                         trust_remote_code=True, device_map="auto", return_full_text=True)

#Dolly Stuff
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline

#template for an instruction with no input
prompt = PromptTemplate(
    input_variables=["instruction"],
    template="{instruction}")

#template for an instruction with input
prompt_with_context = PromptTemplate(
    input_variables=["instruction", "context"],
    template="{instruction}\n\nInput:\n{context}")

hf_pipeline = HuggingFacePipeline(pipeline=generate_text)

llm_chain = LLMChain(llm=hf_pipeline, prompt=prompt)
llm_context_chain = LLMChain(llm=hf_pipeline, prompt=prompt_with_context)


What I don't understand is how will "doc_retriever"  be used in the llm_context_chain or llm_chain variables? 

I noticed no where in my code, I am not calling "doc_retriever". How would I do that? Is there any documentation for uploading your own documentation in Dolly while using HuggingFace? Any help would be greatly appreciated!
### Keywords: embeddings, similarity, sentence, score, embedding, model, label, sentences, use, word