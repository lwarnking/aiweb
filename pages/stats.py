import streamlit as st
import numpy as np

st.header("Stats")

# the highscore and average of score
#st.dataframe(st.session_state.games_won, column_config = {0: "Games Won", 1: "Wrong Guesses"})
st.write("Games won:", st.session_state.games_won)
st.write("Games lost:", st.session_state.games_lost)


# bar chart of guesses for each game
df = np.array([st.session_state.games_won, st.session_state.games_lost])
st.bar_chart(df)

# reset stats
#if st.button("Reset"):
 #   st.session_state.stats.clear()