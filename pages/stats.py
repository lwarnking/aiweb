import streamlit as st
import numpy as np

st.header("Stats")

# data of games played
if "stats" not in st.session_state:
    st.session_state.stats = np.array([])

# the highscore and average of score
st.dataframe(st.session_state.stats)

# bar chart of guesses for each game
st.bar_chart(st.session_state.stats)