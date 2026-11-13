import streamlit as st


# choice = st.radio('Background Type', ['Image', 'Gradient'])

# if choice == 'Image':
#     st.title('Image Background')
#     st.markdown('Boop! :ghost:')

#     image = 'C:/Users/Letic/uni/2026-27_WS/aiweb/middleages.png'

#     css = f'''
#     <style>
#         .stApp {{
#             background-image: url({image});
#             background-size: cover;

#         }}
#         .stApp > header {{
#             background-color: transparent;
#         }}
#     </style>
#     '''
#     st.markdown(css, unsafe_allow_html=True)

# else:
#     st.title('Gradient Background')
#     st.write('Look at the pretty shifting background')

#     with open('else.png') as f:
#         css = f.read()

#     st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

background_image = ""
if st.session_state.age == "middleage":
  background_image = "https://cdn.cosmos.so/2702e9ba-2e68-4e52-94dd-91ebda351e53?format=webp"
elif st.session_state.age == "future":
  background_image = "https://cdn.cosmos.so/0feb6d96-b1d0-49c7-8673-33396107f310.?format=webp"
elif st.session_state.age == "stoneage":
  background_image = "https://cdn.cosmos.so/dceb3917-f148-43b0-831e-91d580edc540?format=webp"
# else:
#   background_image = "https://cdn.cosmos.so/1e4cfa25-efa8-467f-b73c-c282de468d98?format=webp"
#   st.write("Oops, there has been a problem. Please restart the game.")

page_element="""
<style> 
[data-testid="stAppViewContainer"]{
  background-image: url("background_image");
  background-size: cover;
}
</style>
"""


page_element="""
<style> 
[data-testid="stAppViewContainer"]{
  background-image: url("https://cdn.cosmos.so/2702e9ba-2e68-4e52-94dd-91ebda351e53?format=webp");
  background-size: cover;
}
</style>
"""


st.markdown(page_element, unsafe_allow_html=True)



st.write(st.session_state.age)

#let ai generate a fitting word 
# save in variable
# animate fitting letter strokes

# Einzeiliges Text-Eingabefeld
letter = st.text_input("Pick a letter you think is part of this word:")

if letter:
  st.write(f"You think '{letter}' is a good choice?")

# if letter in word = yay
# if not = oh no + hangman animation + sound?


# let ai pick a word

# give option to get more background info on word
# - stats