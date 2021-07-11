from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.backends.backend_agg import RendererAgg
import streamlit as st
import numpy as np
import pandas as pd
import xmltodict
from pandas import *
import urllib.request
import seaborn as sns
import matplotlib
from matplotlib.figure import Figure
from PIL import Image
import gender_guesser.detector as gender
from streamlit_lottie import st_lottie
import requests
import plotly.express as px


def Displaying_data(txt, neg_count, pos_count, nu_count, sentence_array, pol_array, data_dict, headline_text):
    row1, row2 = st.beta_columns((2, 2))
    with row1:

        select = st.sidebar.selectbox(
            'Vizualization type', ['Histogram'], key='1')

        sentiment_count = pd.DataFrame(
            {'polarity': pol_array, 'sentence': sentence_array})

        interactive = st.beta_container()

        with interactive:
            if select == "Histogram":
                fig = px.bar(sentiment_count, x='polarity',
                             color='polarity', height=410, width=350)
                st.plotly_chart(fig)

    with row2:

        st.info("NOTE: The polarity count of individual sentences are as shown in the graph and the maximum value for polarity is considered as the overall sentiment of the article. If any two polarity counts are equal then the model uses the headline for prediction of the overall sentiment.")
        url = "https://hindityping.info/download/assets/Hindi-Fonts-Unicode/gargi.ttf"

        r = requests.get(url, allow_redirects=True)
        font_path = "gargi.ttf"

        with open(font_path, "wb") as fw:
            fw.write(r.content)

            if (pos_count > neg_count) and (pos_count > nu_count):
                largest = pos_count
                text = "  सकारात्मक"
            elif (neg_count > pos_count) and (neg_count > nu_count):
                largest = neg_count
                text = "  नकारातमक"
            elif(pos_count == neg_count) or (pos_count == nu_count) or (neg_count == nu_count) or (neg_count == nu_count == pos_count):
                text = headline_text
            else:
                largest = nu_count
                text = "   तटस्थ"

        wordcloud = WordCloud(max_font_size=50, max_words=100,
                              regexp=r"[\u0900-\u097F]+", background_color="black", font_path=font_path).generate(text)
        wordcloud.generate(text)
        plt.figure(figsize=(350, 300))
        fig, axes = plt.subplots()
        plt.imshow(wordcloud, interpolation="bilinear")

        plt.axis("off")

        st.pyplot(fig)
