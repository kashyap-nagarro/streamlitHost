import streamlit as st
import pandas as pd

title = st.text_input("Movie title", "Life of Brian")
st.write("The current movie title is", title)