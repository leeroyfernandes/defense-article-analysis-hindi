import streamlit as st
import pandas as pd
import numpy as np
#from wordclouddata import Displaying_data
#from indiatv import web_Scrapping
#import plotly.graph_objects as go
# df=pd.DataFrame(
#    np.random.rand(5,2),columns=('Sentence','Polarity')
# )
# st.table(df.style.set_precision(2))


def display_data(des):
    # st.write(des)
    # des1=des.split(".\n")
    data = {
        '': {'Polarity': 'Pos', 'Sentence': des}
    }
    # def color(des):
    #   return ['background-color: green']*len(des) if des.Pos else['background-color: red']*len(des)

    df = pd.DataFrame(data=data).T

    # st.dataframe(df.style.apply(color,subset='Pos'))
    # df.index=[""]*len(df)
    st.table(df)

    #fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    # fig.show()
