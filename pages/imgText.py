import requests
import streamlit as st
import base64
import io
from PIL import Image
import google.generativeai as genai

# Function to convert image file to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set background image
img = get_img_as_base64("C:\\Users\\rjpra\\Desktop\\GUVI AI\\th (1).jpeg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"] {{
background:rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set up API URL and headers for Hugging Face
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Set up Google Gemini AI
genai.configure(api_key="AIzaSyBKWcj-d-jtk5DYe8c3moBv7eTmAssQaJE")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Streamlit interface
st.title("Image Generator and Chatbot")

text_input = st.text_input("Enter your text for both image generation and description")

if st.button("Submit"):
    # Generate image based on the input
    image_bytes = query({"inputs": text_input})
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption='Generated Image')
    
    # After displaying the image, provide a text description
    response = chat.send_message(text_input)
    st.write("Text about the image:")
    st.write(response.text)
