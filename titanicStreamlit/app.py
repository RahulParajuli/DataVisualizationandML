from cProfile import label
import streamlit as st
from predict_page import show_predict_page
from explore_page import *


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    load_data()
    # visuals
