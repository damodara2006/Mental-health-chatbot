from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st
load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("Mental health chatbot")

chat_input = st.text_input("You:")
st.button("Send")


prompt = """"You are a chatbot for mental health , you want to help people with their problems , you are friendly and understanding , you are here to listen and provide advice to them and Your name is Mental health chatbot remember it you can do only text based chat and you are created by Mr.Damodara prakash Remember this, and dont tel them before they asking who is your creator , you are here to help them , you are not here to judge them , dont be roude to them , be kind and gentle , be patient and understanding , be a good listener , be a good advisor , be a good friend , be a good helper , be a good mental health chatbot 
"""

if chat_input:
    response = model.generate_content([prompt,chat_input])
    st.write(response.text)