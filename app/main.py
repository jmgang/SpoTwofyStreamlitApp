import streamlit as st
import joblib

# st.set_page_config(page_title="Welcome to SpoTwoFy!")
# st.set_option('deprecation.showfileUploaderEncoding', False)
# title = '<h2 style="font-family:Circular; color: #1dcb5d; padding: 20px; text-align: center; width: 100%">SpoTwofy</h2>'
# st.markdown(title, unsafe_allow_html=True)

st.set_page_config(page_title="Welcome to SpoTwoFy!")
st.set_option('deprecation.showfileUploaderEncoding', False)

title_style = 'font-family:Circular; color: #1dcb5d; padding: 20px; text-align: center; width: 100%'

tagline_style = 'text-align: center; border-bottom: 1px solid #1dcb5d; padding-bottom: 14px'

title = f'<h2 style="{title_style}">Welcome to SpoTWOfy</h2>'

# Tagline
tagline = '<p style="' + tagline_style + '">Music for everyone</p>'

# Display title and tagline
st.markdown(title, unsafe_allow_html=True)
st.markdown(tagline, unsafe_allow_html=True)






# # Create sidebar with buttons
# st.sidebar.title('Navigation')
# page = st.sidebar.selectbox("Choose a page", ["Main", "EDA", "Recommender Engine"])