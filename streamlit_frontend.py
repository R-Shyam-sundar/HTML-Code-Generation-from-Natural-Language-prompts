import streamlit as st
import requests
import time
import random
import string
import wave
import glob

st.title("Figr Assignment - HTML Code generation")

training_message = st.empty()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your queries here.."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    # Make API request to FastAPI server
    api_url = "https://bc11-34-142-217-209.ngrok-free.app/html_code_generation"
    data = {"Question": prompt}
    
    response = requests.post(api_url, json=data)
    print(response)
    if response.status_code == 200:
        answer = response.json()
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown(answer + "▌")
            message_placeholder.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
