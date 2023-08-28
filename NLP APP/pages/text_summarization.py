import streamlit as st

from txtai.pipeline import Summary
from PyPDF2 import PdfReader


@st.cache_resource
def summary_text(text):
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

# extract text from the pdf using PyPDF2
# def extract_text_from_pdf(file_path):
#    with


st.set_page_config(layout="wide")
choice = st.selectbox("Select your choice" , ["Summarize Document" , "Summarize text"])

if choice=="Summarize text":
    st.subheader("Summarize Text")
    input_text = st.text_area("enter your text here" , height=300)
    if input_text:
        if st.button("Summarize"):
           col1 , col2 = st.columns([1,1])

           with col1:
            st.markdown("**Your Input Text**")
            st.info(input_text)

           with col2:
            result = summary_text(input_text)
            st.markdown("**Summarized Text**")
            st.success(result)



elif choice=="Summarize Document":
    st.subheader("Summarize Document")
    input_file = st.file_uploader("Upload your document" , type=["pdf" , "txt"])
    if input_file is not None:
       if st.button("Summarize"):
        pass  