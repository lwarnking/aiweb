import streamlit as st

# counter for won games
if "games_won" not in st.session_state:
  st.session_state.games_won = 0

# counter for lost games
if "games_lost" not in st.session_state:
  st.session_state.games_lost = 0

col1, col2 = st.columns(2)

with col1:
  st.image("Hangman14.jpg", width=300)

with col2:
  st.header(":blue[Hangman] through Time")
  st.write("Have ultimate fun!!!")
  if st.button("**Play!**"):
      st.switch_page("pages/choose your player.py") 
  
  if st.button("View Stats"):
      st.switch_page("pages/stats.py")

# data of games played
if "stats" not in st.session_state:
    st.session_state.stats = [] 
  