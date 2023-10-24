import streamlit as st
import joblib

st.set_page_config(page_title="SpoTwoFy")
st.set_option('deprecation.showfileUploaderEncoding', False)
title = '<h2 style="font-family:Arial; background: #1abc9c; color: white; padding: 20px; text-align: center; width: 100%">SpoTwofy</h2>'
st.markdown(title, unsafe_allow_html=True)


# Create sidebar with buttons
st.sidebar.title('Navigation')
page = st.sidebar.selectbox("Choose a page", ["Home", "EDA", "Recommender Engine"])