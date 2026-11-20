import streamlit as st
import numpy as np

st.header("Stats")

# data of games played
stats = np.array([])

# the highscore and average of score
st.dataframe(stats)

# bar chart of guesses for each game
st.bar_chart(stats)