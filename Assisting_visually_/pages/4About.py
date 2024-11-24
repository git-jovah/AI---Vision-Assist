import streamlit as st


st.title("About me")
with st.container(border=True):
    col1,col2 = st.columns([0.2,0.8])
    with col1:
        st.image("logo/linkedIn.png")
    with col2:
        st.write("<h5>linkedIn</h5>",unsafe_allow_html=True)
        st.markdown('<a href="https://www.linkedin.com/in/jawaharjovah/">visit linkedin</a>',unsafe_allow_html=True)

with st.container(border=True):
    col3,col4 = st.columns([0.2,0.8])
    with col3:
        st.image("logo/GitHub-logo.png")
    with col4:
        st.write("<h5>GitHub</h5>",unsafe_allow_html=True)
        st.markdown('<a href="https://github.com/git-jovah">visit git</a>',unsafe_allow_html=True)

with st.container(border=True):
    col5,col6 = st.columns([0.2,0.8])
    with col5:
        st.image("logo/medium.jpeg")
    with col6:
        st.write("<h5>Medium</h5>",unsafe_allow_html=True)
        st.markdown('<a href="https://medium.com/@jawaharjovah2003">visit medium</a>',unsafe_allow_html=True)

