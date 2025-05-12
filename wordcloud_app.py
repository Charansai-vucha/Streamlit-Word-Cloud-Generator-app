# wordcloud_app.py

import streamlit as st
from wordcloud import WordCloud
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Configure the page layout and title
st.set_page_config(page_title="Word Cloud Generator", page_icon="☁️", layout="centered")

# App header
st.header("Word Cloud Generator ☁️")

# Input selection: Text or URL
input_type = st.radio("Select input type", ("Text", "URL"))

# Variable to store the final text
text = ""

# Handle input based on selection
if input_type == "Text":
    text_input = st.text_area("Enter text here")
    text = text_input

elif input_type == "URL":
    url_input = st.text_input("Enter URL here")
    if url_input:
        try:
            response = requests.get(url_input)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
        except Exception as e:
            st.error(f"Error fetching or parsing URL: {e}")

# Button to generate word cloud
generate_button = st.button("Generate Word Cloud")

# Generate and display the word cloud if button clicked
if generate_button and text:
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
