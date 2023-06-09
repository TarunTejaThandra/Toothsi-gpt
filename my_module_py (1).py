# -*- coding: utf-8 -*-
"""my_module.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xrKKEItuvAHoqsmVJan63hIDq3wZi5tB
"""

#!pip install llama-index                                                                    # Installs the llama-index package, which provides an implementation of the LSH algorithm for approximate nearest neighbor search
#!pip install langchain    
# Import necessary modules
from llama_index import Document                     # Imports the Document class from the llama-index package
from llama_index import SimpleDirectoryReader        # Imports the SimpleDirectoryReader class from the llama-index package
from llama_index.node_parser import SimpleNodeParser # Imports the SimpleNodeParser class from the llama-index package
from llama_index import GPTSimpleVectorIndex  # Imports the GPTSimpleVectorIndex class from the llama-index package
import sys                                    # Imports the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import os                                     # Imports the os module, which provides a way of using operating system dependent functionality like reading or writing to the file system
from IPython.display import Markdown, display # Imports Markdown and display functions from IPython.display module to display formatted output
import shutil                                 # Imports the shutil module, which provides a higher level interface when working with files

from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI
import sys
import shutil 
import os
from IPython.display import Markdown, display
from llama_index.data_structs.node_v2 import Node, DocumentRelationship
import os
from textacy import Document

def construct_index(directory_path): # Define a function to construct the index
    
    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

      # define prompt helper
      # set maximum input size
    max_input_size = 4096
      # set number of output tokens
    num_output = 256
      # set maximum chunk overlap
    max_chunk_overlap = 20


    # Create a new PromptHelper object with the specified parameters
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    # Create a new ServiceContext object with the default parameters, including a reference to the LLM Predictor and the PromptHelper object
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    # Create a new GPTSimpleVectorIndex object from the specified documents and ServiceContext object
    index = GPTSimpleVectorIndex.from_documents(
        documents, service_context=service_context
    )


    # Save the index to disk as a JSON file
    index.save_to_disk('index.json')
     
    # Return the index object 
    return index

# Define a function to query the index and generate a response
def ask_ai():
    # Load the index from the JSON file on disk
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        # Prompt the user for a query
        query = input("What do you want to ask? ")
        # Query the index and generate a response
        response = index.query(query, response_mode="compact")
        # Display the response using Markdown formatting
        display(Markdown(f"Response: <b>{response.response}</b>"))