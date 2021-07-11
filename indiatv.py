from bs4 import BeautifulSoup
import streamlit as st
import requests
import csv
import pandas as pd
from csv import reader
from trial import display_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import numpy as np
import pandas as pd
from wordclouddata import Displaying_data
import operator

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

vocab_f = open("vocab.pickle", "rb")
vocab = pickle.load(vocab_f)
vocab_f.close()

vect = CountVectorizer(vocabulary=vocab)


def web_Scrapping_indiatv(urls):
    st.markdown("<h1 style='text-align: center; color: silver;'>Article Analysis</h1>",
                unsafe_allow_html=True)
    summary = []
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)'
    }

    for row in urls:
        if operator.contains(row, "https://www.indiatv.in/"):
            st.text_input("URL", row)
            response = session.get(row, headers=headers)
            source = requests.get(row).text
            soup = BeautifulSoup(source, 'lxml')
            headline_ele = soup.find(class_='artsubject')
            print("Headline")
            headline = st.text_input("Headline", headline_ele.text)
            description_ele = soup.find(class_='content')
            st.write("  ")
            description = description_ele.find_all("p")
            for item in description:
                summary.append(item.text)
            str1 = ''.join(summary)
            x = str1.split('।')

            y = str1.replace("।", ".\n")
            print(y)
            st.text_area("Description", y, 500)

            y.split('.')
            # Sentence_break = y.replace('.', '.\n')

            df = pd.DataFrame({'Headline': [headline]})
            Y = df['Headline']
            headline_test_dtm = vect.transform(Y)
            headline_predictions = classifier.predict(headline_test_dtm)
            if (headline_predictions == "pos"):
                text = "  सकारात्मक"
            elif(headline_predictions == "neg"):
                text = "  नकारातमक"
            else:
                text = "   तटस्थ"

            a = []
            pol = []
            for line in x:
                print(line)
                df = pd.DataFrame({'Description': [line]})
                X = df['Description']
                X.shape
                X_test_dtm = vect.transform(X)
                X_test_dtm
                test_predictions = classifier.predict(X_test_dtm)
                str1 = " ".join(test_predictions)

                a.append(line)
                pol.append(str1)
                # Dict = dict({line: test_predictions})
                # st.write(line)
                # st.write(test_predictions)

            pol.pop()
            a.pop()

            negative = pol.count("neg")
            positive = pol.count("pos")
            neutral = pol.count("nu")

            print(negative)
            print(positive)
            print(neutral)

            dictionary = dict(zip(a, pol))
            print(dictionary)

            st.write(dictionary)
            # st.write("\t\t\t\tPolarity")
            # cols = st.beta_columns(4)

            # cols[0].write(y)

            # cols[2].write("Polarity")

            # st.write(len(y))
            st.markdown("""<br>""", True)
            # display_data(Sentence_break)
            Displaying_data(y, negative, positive, neutral,
                            a, pol, dictionary, text)
        else:
            st.error("     Please Enter a valid URL for selected news agency")
