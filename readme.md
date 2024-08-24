# Rag model to create chat assistant 

## Overview

 A simple fine tuned RAG (retrieval augmented generation) model which is able to answer user
 queries for tymeline and creating a chatbot from it.

## Setup to run the chatbot
Clone the repositry from this link
```bash
git clone https://github.com/csoham96/rag
```
Install the environment ,ensure you have miniconda or anaconda install
```bash
conda env create --file environment.yml
```

Activate the environment
```bash
conda activate  rag
```

Ensure you login with your huggingface 

Run the following command to launch the streamlit app,
it will take some time to download the model and then once its done, the setup is complete

```bash
streamlit run app.py
```
# Alternative

If you want to run a rag model from PDF file and query it, make sure to install following commands to install library
## Install ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3.1
```

This will download and install ollama library which will download the llama 3.1 8billion model which can run natively in our pc with a decent gpu

## Install some libraries

```bash
pip install langchain langchain-community
```

Then run the chatbot
```bash
streamlit run rag.py
```

This is basically a conversational chatbot which reads the pdf file converts the texts of the pdfs into embedings stores in a vector DB and then the llm queries information regarding the pdf from the vector db.
It all runs locally so our data remains secure.

# Dataset creation process and model building
I have gathered multiple sources of text from tymeline website and other places and made them into question answer context triplet,
Used that data to fine tune an llm ( llama 3 instruct model )and Lora to build on top of it and merged the models.
Then created custom prompts to generate appropriate outputs.The model which i trained was in colab but due to some cuda out of memory issues wasnt able to merge with llm model,
but the model building code is present in the python notebook RagModel.ipynb which can be used to replicate the steps to build model provide we have enough gpu space.
Dataset is in data folder
