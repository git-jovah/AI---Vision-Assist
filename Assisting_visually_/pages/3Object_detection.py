import streamlit as st
from main import function

st.title("Object detection")
image = st.file_uploader("upload image",type=["jpg","png","jpeg"])
if image:
    st.image(image=image)
    function(image,"obj_det")