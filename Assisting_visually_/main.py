
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai
import streamlit as st
from PIL import Image
import pyttsx3


engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

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
    

    try:
        img = Image.open(img)
        if destiny:
            response = chat_model.generate_content([img,query_dict[destiny]])
            st.markdown(response.text)
            if destiny == "camera":
                pass
            else:
                if st.button("voice assist"):
                    engine.endLoop()
                    text_to_speech(response.text)
                if st.button("stop voice assist"):
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

    chain = chat_propt_template | chat_model | output_parsers
    user_input = {"topic":topic}
    response = chain.invoke(user_input)
    with st.chat_message("human"):
        st.write(topic)
    with st.chat_message("assistant"):
        st.markdown(response,unsafe_allow_html=True)

if __name__ == "__main__":
    pass

    