import streamlit as st
import pandas as pd
import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from wordclouddata import Displaying_data
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle
import operator

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

vocab_f = open("vocab.pickle", "rb")
vocab = pickle.load(vocab_f)
vocab_f.close()

vect = CountVectorizer(vocabulary=vocab)


def web_Scrapping_aajtak(urls):
    st.markdown("<h1 style='text-align: center; color: silver;'>Article Analysis</h1>",
                unsafe_allow_html=True)
    for url in urls:
        if operator.contains(url, "https://www.aajtak.in/"):
            page = requests.get(url)
            page.text
            soup = BeautifulSoup(page.text, 'html.parser')
            soup.find('div', class_='fedback-sec').decompose()
            headline_ele = soup.find("div", {'class': "content-area"}).h1.text
            print("headline:", headline_ele)
            print("\n")

            print("DESCRIPTION")
            print("\n")

            description_name = []
            description_ele = soup.find_all("p")
            description_ele.pop()

            for item in description_ele:
                description_name.append(item.text)

            str1 = ''.join(description_name)

            x = str1.split('.')

            print("***********")

            print("\n")
            y = str1.replace(".", ".\n")

            print(y)
            print(url)
            st.text_input("URL", url)
            headline = st.text_input("Headline", headline_ele)

            st.text_area("Description", y, 1000)

            print("\n")

            Sentence = y.replace('.', '.\n')

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

            st.markdown("""<br>""", True)

            Displaying_data(y, negative, positive, neutral,
                            a, pol, dictionary, text)

        else:
            st.error("     Please Enter a valid URL for selected news agency")
