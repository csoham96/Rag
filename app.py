from transformers import AutoModelForCausalLM, AutoTokenizer,pipeline
import streamlit as st
from textwrap import dedent
MODEL_NAME = "curiousily/Llama-3-8B-Instruct-Finance-RAG"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto"
)

pipe = pipeline(
    task="text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128,
    return_full_text=False,
)

def create_test_prompt(data_row):
    prompt = dedent(f"""
    {data_row["question"]}

    Information:

    ```
    {data_row["context"]}
    ```
    """)
    messages = [
        {"role": "system", "content": "Use only the information to answer the question"},
        {"role": "user", "content": prompt},
    ]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)


st.title("Chatbot for tymeline")

user_input = st.text_area("Enter your query regarding tymeline")

if st.button("Predict"):
    if user_input:

        prompt=create_test_prompt(user_input)
        prediction=pipe[prompt]
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Please enter some text!")
