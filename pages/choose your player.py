import streamlit as st
import time

if "age" not in st.session_state:
    st.session_state.age = ""

stoneage, middleage, future = st.columns(3)
if stoneage.button("choose stoneage", icon=":material/cruelty_free:",width="stretch"):
    st.session_state.age = "stoneage"
    stoneage.markdown("Let's head back to the stoneage")
    with st.spinner("time travel loading..."):
        st.session_state.key = 'stoneage'
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py") 
if middleage.button("choose middleage", icon="😃", width="stretch"):
    st.session_state.age = "middleage"
    middleage.markdown("Let's head into the middleage")
    with st.spinner("time travel loading..."):
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py")
if future.button("choose newage", icon=":material/mood:", width="stretch"):
    st.session_state.age = "future"
    future.markdown("Let's head into the future")
    with st.spinner("time travel loading..."):
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py")


