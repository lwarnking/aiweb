import streamlit as st
import numpy as np

st.header("Stats")

# the highscore and average of score
st.dataframe(st.session_state.stats, column_config = {0: "Games Won", 1: "Wrong Guesses"})

# bar chart of guesses for each game
st.bar_chart(st.session_state.stats)

# reset stats
if st.button("Reset"):
    st.session_state.stats.clear()