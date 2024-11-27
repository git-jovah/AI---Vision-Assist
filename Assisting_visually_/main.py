
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai
import streamlit as st
from PIL import Image
import pyttsx3
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
engine = pyttsx3.init()

def text_to_speech(text):
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        st.warning("There is no text in the image!")
        
    

file = r"E:\\Assisting_visually_\\key.txt"
with open(file,"r") as f:
    Google_Api_Key = f.readline()
    

def function(img,destiny: str):
    query_dict = {
        "camera":"explain everything in the picture?",
        "obj_det":"what objects or things do you see in this picture and Object and Obstacle Detection for Safe Navigation",
        "auto": "what you see in the picture recognizing items, reading labels, or providing context-specific information."
    }
        
    genai.configure(api_key=Google_Api_Key)
    
    chat_model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    
    col1, col2 = st.columns(2)
    try:
        img = Image.open(img)
        extracted_text = pytesseract.image_to_string(img)
        if destiny:
            response = chat_model.generate_content([img,query_dict[destiny]])
            st.markdown(response.text)
            if destiny in ("camera", "auto", "obj_det"):
                with col1:
                    if st.button(":green[start] voice assist",use_container_width=True):
                        if engine._inLoop:
                            engine.endLoop()
                            text_to_speech(response.text)
                        else:
                            text_to_speech(response.text)
                        
                with col2:
                    if st.button(":red[stop] voice assist",use_container_width=True):
                        engine.stop()
                
            else:
                with col1:
                    if st.button(":green[start] voice assist",use_container_width=True):
                        if engine._inLoop:
                            engine.endLoop()
                            text_to_speech(extracted_text)
                        else:
                            text_to_speech(extracted_text)
                        
                with col2:
                    if st.button(":red[stop] voice assist",use_container_width=True):
                        engine.stop()
            
    except Exception as e:
        st.error(f"error occurred:{e}")


# langchain
def langch(topic):
    chat_model = ChatGoogleGenerativeAI(google_api_key = Google_Api_Key,model="models/gemini-1.5-flash")
    output_parsers = StrOutputParser()

    chat_propt_template = ChatPromptTemplate.from_messages([
       ("system", "you are helpful assistant"),
       ("human", "{topic}?"),
    ])

    if 'history' not in st.session_state:
        st.session_state.history = []
    for message in st.session_state.history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    st.session_state.history.append({"role":"user","content":topic})

    chain = chat_propt_template | chat_model | output_parsers
    user_input = {"topic":topic}
    response = chain.invoke(user_input)
    with st.chat_message("human"):
        st.write(topic)
    with st.chat_message("assistant"):
        st.markdown(response,unsafe_allow_html=True)
    st.session_state.history.append({"role":"ai","content":response})

    

if __name__ == "__main__":
    pass

    
