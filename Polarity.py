import streamlit as st
import pandas as pd
import numpy as np
import csv
import base64
from indiatv import *
from aajtak import *
from tv9 import *
from subprocess import call
from ndtvscrapper import *
from csv import reader
import operator


def Polarity():
    select_option = ['NDTV Article', 'INDIATV Article',
                     'AAJTAK ARTICLE', 'TV9 ARTICLE']
    page = st.sidebar.radio('', select_option)
    if page == 'NDTV Article':
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>NDTV Article</h3>", unsafe_allow_html=True)
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
        name1 = st.sidebar.text_input("", "https://")
        ana = st.sidebar.button("Analyze")
        name = ([name1])
        if ana:
            url = name
            # st.write(url)
            # url.append(name)
            # filename='data.csv'
            # with open(filename,'w') as csvwrite:
            #   csvwriter=csv.writer(csvwrite,delimiter='-')
            #  csvwriter.writerow(name)

            # if operator.contains(url, "https://ndtv.in/"):
            # Web_Scrapper_ndtv(url)
            # else:
            # st.error("Please Enter Valid Url")
            Web_Scrapper_ndtv(url)

    elif page == 'INDIATV Article':
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>INDTV Article</h3>", unsafe_allow_html=True)
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
        name2 = st.sidebar.text_input("", "https://")
        ana1 = st.sidebar.button("Analyze")
        name3 = ([name2])
        if ana1:
            url = name3
           # st.write(url)
            web_Scrapping_indiatv(url)

    elif page == 'AAJTAK ARTICLE':
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>AAJTAK Article</h3>", unsafe_allow_html=True)
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
        name2 = st.sidebar.text_input("", "https://")
        ana1 = st.sidebar.button("Analyze")
        name3 = ([name2])
        if ana1:
            url = name3
           # st.write(url)
            web_Scrapping_aajtak(url)

    else:
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>TV9 Article</h3>", unsafe_allow_html=True)
        st.sidebar.markdown(
            "<h3 style='text-align: center; color: yellow;'>Paste the URL of the Article</h3>", unsafe_allow_html=True)
        name2 = st.sidebar.text_input("", "https://")
        ana1 = st.sidebar.button("Analyze")
        name3 = ([name2])
        if ana1:
            url = name3
           # st.write(url)
            web_Scrapping_tv9(url)
