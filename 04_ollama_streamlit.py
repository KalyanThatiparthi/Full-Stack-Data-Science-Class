import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")
st.title("MY First Chatbot App")
st.header("Ask Chatbot Anything!")
prompt=st.text_area("Enter your Prompt here", height=200)
if st.button("Click here to Generate Response"):
    if prompt=="minimax-m2.7:cloud":
        st.warning("Please enter a valid prompt to get a response from Ollama.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(model="minimax-m2.7:cloud", messages=[{"role": "user", "content": prompt}])
            st.success("Response generated successfull2y!")
            st.write(response["message"]["content"])
