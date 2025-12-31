import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter your text")

source_lang = st.selectbox(
    "Select Source Language",
    ["auto", "en", "ta", "hi", "fr"]
)

target_lang = st.selectbox(
    "Select Target Language",
    ["en", "ta", "hi", "fr"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)
    
    st.success(translated)