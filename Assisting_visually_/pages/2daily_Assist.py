import streamlit as st
from main import function,langch

st.title("Personalized Assistance")
image = st.file_uploader("upload image",type=["jpg","png","jpeg"])
if image:
    st.image(image=image)
    function(image,"auto")

chat = st.chat_input("Enter message..")
if chat:
    langch(chat)