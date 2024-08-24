import streamlit as st
import google.generativeai as genai

st.title("Welcome to My Search Bar")

genai.configure(api_key="AIzaSyBKWcj-d-jtk5DYe8c3moBv7eTmAssQaJE")

text = st.text_input("enter Your Question")

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)
