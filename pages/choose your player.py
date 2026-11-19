import streamlit as st
import time

if "age" not in st.session_state:
    st.session_state.age = ""
    
stoneage, middleages, future = st.columns(3,vertical_alignment="center")

if stoneage.button("choose stoneage", icon=":material/cruelty_free:",width="stretch"):
    st.session_state.age = "stoneage"
    stoneage.markdown("Let's head back to the stoneage")
    with st.spinner("time travel loading..."):
        st.session_state.key = 'stoneage'
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py") 

if middleages.button("choose middleages", icon="😃", width="stretch"):
    st.session_state.age = "middleage"
    middleages.markdown("Let's head into the middleages")
    with st.spinner("time travel loading..."):
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py")

if future.button("choose future", icon=":material/mood:", width="stretch"):
    st.session_state.age = "future"
    future.markdown("Let's head into the future")
    with st.spinner("time travel loading..."):
        time.sleep(5)  # Delay for 5 seconds
        st.switch_page("pages/game.py")





