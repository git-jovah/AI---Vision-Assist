import streamlit as st
from main import function
from PIL import Image
import base64 

st.title(":blue[AI] :red[-] Vision Assist")

def set_background(png_file):
    bin_str = open(png_file, 'rb').read()
    encoded = base64.b64encode(bin_str).decode()
    background_color_css = f""" 
        <style> 
        .stApp {{background-image: url("data:image/png;base64,{encoded}");
            background-size: cover; 
            background-repeat: no-repeat;
            background-attachment: fixed;
            
        }} 
        </style>
    """
    st.markdown(background_color_css, unsafe_allow_html=True)
set_background('vibrant.png')
def main():

    # Style buttons with custom CSS if needed
    st.markdown(
        """
        <style>
        div.stButton button {
            color: #bbe7fc;
            background-color: rgba(255,255,255,0.2); /*255,255,255*/
            height: 205px;
            width: 300px;
            margin: 10px;
            border-color: white;
            border-radius: 10px;
            transition: all 0.3s ease;

        }
        div.stButton button:hover {
            color: white;
            border-color: gray;
            box-shadow: inset 3px 3px 10px rgba(255, 255, 255, 0.5);
            width: 290px;
            height: 190px;
        }

        
        </style>
        """,
        unsafe_allow_html=True
    )

    col_num=[0.5,0.5]
    b1,b2 = st.columns(col_num)
    b3,b4 = st.columns(col_num)
    # Real-time scene understanding.
    # ● Text-to-speech conversion for reading visual content.
    # ● Object and obstacle detection for safe navigation.
    # ● Personalized assistance for daily tasks.
    with b1:
        if st.button("Camera"):
            st.switch_page("pages/1camera.py")
    with b2:
        if st.button("Daily Assist"):
            st.switch_page("pages/2daily_Assist.py")
    with b3:
        if st.button("Object detection"):
            st.switch_page("pages/3Object_detection.py")
    with b4:
        if st.button("About"):
            st.switch_page("pages/4About.py")
    

    st.sidebar.markdown(
        '''
        A Gemini based Application,     
        by :blue[Jawahar Jovah]

'''
    )

if __name__ == "__main__":
    main()