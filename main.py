import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
import altair as alt
#from streamlit_option_menu import option_menu
from joblib import load
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

showWarningOnDirectExecution = False

st.title('Portal Tugas UAS Berita PPW')

st.write("Oleh | Aulya Miftahkhul Hikmah | 200411100050")
tab1, tab2, tab3, tab4 = st.tabs(["Data Mentah", "Preprocessing","Summary", "Modelling"])


# ====================== Crawling ====================
with tab1:
        dataset = pd.read_csv("https://raw.githubusercontent.com/aulyamiftahkhulhikmah/Dataset/main/CrawlingBerita%20(2).csv")
        st.dataframe(dataset)
        st.info(f"Banyak Dataset : {len(dataset)}")
        st.warning(f'Informasi Dataset')
        st.write(dataset.describe())


with tab2:
        dataset = pd.read_csv("https://raw.githubusercontent.com/aulyamiftahkhulhikmah/Dataset/main/DatasummaryRadarJatim.csv")
        st.dataframe(dataset)
        st.info(f"Banyak Dataset : {len(dataset)}")
        st.warning(f'Informasi Dataset')
        st.write(dataset.describe())


with tab3:
        dataset = pd.read_csv("https://raw.githubusercontent.com/aulyamiftahkhulhikmah/Dataset/main/DataSummaryBerita.csv")
        
        st.dataframe(dataset)
        st.info(f"Banyak Dataset : {len(dataset)}")
        st.warning(f'Informasi Dataset')
        st.write(dataset.describe())

with tab4:
        dataset = pd.read_csv("https://raw.githubusercontent.com/aulyamiftahkhulhikmah/Dataset/main/hasilPrediksi.csv")
        
        st.dataframe(dataset)
        st.info(f"Banyak Dataset : {len(dataset)}")
        st.warning(f'Informasi Dataset')
        st.write(dataset.describe())

    












