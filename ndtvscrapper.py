from trial import display_data
import streamlit as st
import pandas as pd
import requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from wordclouddata import Displaying_data
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import operator

classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

vocab_f = open("vocab.pickle", "rb")
vocab = pickle.load(vocab_f)
vocab_f.close()

vect = CountVectorizer(vocabulary=vocab)


def Web_Scrapper_ndtv(urls):

    st.markdown("<h1 style='text-align: center; color: silver;'>Article Analysis</h1>",
                unsafe_allow_html=True)
    for url in urls:
        if operator.contains(url, "https://ndtv.in/"):
            page = requests.get(url)
            page.text
            soup = BeautifulSoup(page.text, 'html.parser')
            soup.find('p', class_='ft-social--txt').decompose()
            soup.find('div', class_='ft-social--wrap').decompose()
            soup.find('div',  attrs={'id': 'jiosaavn-widget'}).decompose()
            soup.find('div',  attrs={'class': 'ins_instory_dv'}).decompose()

            soup.find('aside', class_='col-300').decompose()
            soup.find('div',  attrs={'class': 'reltd-main'}).decompose()

            headline_ele = soup.find("div", {'class': "sp-ttl-wrp"}).h1.text
            print("headline:", headline_ele)
            print("\n")

            print("DESCRIPTION")
            print("\n")

            description_name = []
            description_ele = soup.find_all("p")

            for item in description_ele:
                description_name.append(item.text)

            str1 = ''.join(description_name)

            x = str1.split('.')
            y = str1.replace(".", ".\n")

            print(y)
            print(url)
            st.text_input("URL", url)
            headline = st.text_input("Headline", headline_ele)

            st.text_area("Description", y, 500)

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
            # cols = st.beta_columns(3)
            # cols[0].write(Sentence)
            # cols[2].write("Polarity")
            # st.write(len(y))

        # if st.button("Anaalyze in Detail"):
         #   annalyze_in_detail(Sentence)
            # st.write(len(y))

            st.markdown("""<br>""", True)
            # display_data(Sentence_break)
            Displaying_data(y, negative, positive, neutral, a,
                            pol, dictionary, text)

        else:
            st.error("     Please Enter a valid URL for selected news agency")
