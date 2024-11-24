import streamlit as st
from PIL import Image
from main import function

st.title("camera")
pic = st.camera_input("Take live photo and generate text:")
if pic:
    if st.button("process and generate",use_container_width=True):
        function(pic,"camera")