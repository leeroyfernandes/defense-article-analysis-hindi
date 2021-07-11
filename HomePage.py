import streamlit as st
import pandas as pd
import numpy as np
import base64
from Polarity import *
from Headline import *

main_bg = "Polarity.jpg"
main_bg_ext = "jpg"

st.sidebar.title("Polarity Classification")
st.sidebar.markdown(
    "<h3 style= color: white;'>Select a News Agency</h3>", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-image: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover;
        background-repeat: no-repeat;        

    }}
    

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h1 style='text-align: center; color: white;'>Sentiment Analysis Of Defense News Articles(Hindi)</h1><br>",
            unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: lightslategray;'>A UI based Model to find the polarity of hindi defense articles based on the sentiment of individual sentences in the article</h4>", unsafe_allow_html=True)


Polarity()


# Headline()
