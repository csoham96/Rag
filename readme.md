# Rag model to create chat assistant 

## Overview

 A simple fine tuned RAG (retrieval augmented generation) model which is able to answer user
 queries for tymeline and creating a chatbot from it.

## Setup to run the chatbot
Clone the repositry from this link
```bash
git clone 
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

# Dataset creation process and model building
I have gathered multiple sources of text from tymeline website and other places and made them into question answer context triplet,
Used that data to fine tune an llm ( llama 3 instruct model )and Lora to build on top of it and merged the models.
Then created custom prompts to generate appropriate outputs.The model which i trained was in colab but due to some cuda out of memory issues wasnt able to merge with llm model,
but the model building code is present in the python notebook RagModel.ipynb which can be used to replicate the steps to build model provide we have enough gpu space.
Dataset is in data folder