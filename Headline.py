import streamlit as st
import pandas as pd
import numpy as np
import base64

st.markdown(
    f"""
    <style>
    

    </style>
    """,
    unsafe_allow_html=True
)


def Headline():

    st.markdown("<h1 style='text-align: center; color: white;'>Headline Classification </h1>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: yellow;'>Paste the Hedline  of the Article</h3>",
                unsafe_allow_html=True)
    name = st.text_input("", "")
    if st.button("Analyze to "):

        # Bollywood Headline
        st.error("Bollywood")

    # Defense based Headline
        st.success("Defense")

    # Sports Based Headline
        st.info("Sports")
