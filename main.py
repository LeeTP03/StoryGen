import streamlit as st
from gpt import *

st.write("# Story Generator")

title = st.text_input("Give a plot")

if st.button("Generate a story "):
  story, url = story_with_cover(title)

  st.image(url)
  st.write(story)