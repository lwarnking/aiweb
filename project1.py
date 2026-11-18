import streamlit as st

guesses = 6
link = "'"+"Hangman" + str(6) + ".jpg" + "'"
st.image(
    link,
    caption="your current closeness level to death",
)