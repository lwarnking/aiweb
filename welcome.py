import streamlit as st

st.title("Welcome to :blue[Hangman]", 
         icon=":material/thumb_up:",
         text_alignment="right")

st.write("have fun")

if st.button("Go to Game"):
  st.switch_page("pages/choose your player.py") 
