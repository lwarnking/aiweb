import streamlit as st
import time
from string import Template

# page layout full screen
st.set_page_config(layout="wide")

# if not provided by page beforehand, result in warning
if "age" not in st.session_state:
    st.session_state.age = ""


# individual background images for each theme
background_images = ""
if st.session_state.age == "stoneage":
  tostop = "no"
  page_element="""
  <style> 
  [data-testid="stAppViewContainer"]{
    background-image: url("https://cdn.cosmos.so/dceb3917-f148-43b0-831e-91d580edc540?format=webp");
    background-size: cover;
  }
  </style>
  """
elif st.session_state.age == "middleage":
  tostop = "no"
  page_element="""
  <style> 
  [data-testid="stAppViewContainer"]{
    background-image: url("https://cdn.cosmos.so/2702e9ba-2e68-4e52-94dd-91ebda351e53?format=webp");
    background-size: cover;
  }
  </style>
  """
elif st.session_state.age == "future":
  tostop = "no"
  page_element="""
  <style> 
  [data-testid="stAppViewContainer"]{
    background-image: url("https://cdn.cosmos.so/0feb6d96-b1d0-49c7-8673-33396107f310.?format=webp");
    background-size: cover;
  }
  </style>
  """
else:
  tostop = "yes"
  page_element="""
  <style> 
  [data-testid="stAppViewContainer"]{
    background-image: url("https://cdn.cosmos.so/01a19d13-d1b9-76c9-9aca-f87e3f16e5a6?format=webp");
    background-size: cover;
  }
  </style>
  """

# background image
st.markdown(page_element, unsafe_allow_html=True)


# if page crashes and session_states are lost
if not tostop == "no":
  st.set_page_config(layout="centered")
  st.warning('Oops, there has been a problem. Please go back in time and restart the game.')
  st.stop()


# header
st.markdown(
    f"""
    #### <h1 style='text-align: center;'> Welcome to the <span style="color:orange">{st.session_state.age}</span> </h1> 
    """,
    unsafe_allow_html=True,
)


st.space("medium")

# horizontal placement of different game parts
col1, col2, col3 = st.columns([1, 2, 1],wrap=False)

# visualization of hangman image (later animation based on game status)
with col1:
    if "wrong_guesses" not in st.session_state:
      st.session_state.wrong_guesses = ""
    if len(st.session_state.wrong_guesses) == 0:
      link = "Hangman13.jpg"
    elif len(st.session_state.wrong_guesses) > 0:
      link = "Hangman" + str(len(st.session_state.wrong_guesses)) + ".jpg"
    #link = "Hangman6.jpg"
    st.image(
      link,
      caption="your current closeness level to death",
)
# letter guessing input
with col2:
    letter = ""
    letters = st.chat_input("Pick a letter you think is part of this word")
    if letters:
      letter = letters
    
    # hardcoded rn, later provided by ai, max 10 letters
    word = "outerspace"

    # list for all guessed letters
    if "letterlist" not in st.session_state:
        st.session_state.letterlist = []
    
    # list for correctly guessed letters
    if "correctlist" not in st.session_state:
        st.session_state.correctlist = []

    # list of correct letter indices
    if "indiceslist" not in st.session_state:
        st.session_state.indiceslist = []
  

    # letter input through player
    #letter = st.text_input(f"**Pick a letter you think is part of this word:**")
    st.session_state.letterlist.extend(letter)
    
    # list of indices of correct letters
    indices = [i for i, ch in enumerate(word) if ch == letter]
    st.session_state.indiceslist.extend(indices)
    if letter in word:
       st.session_state.correctlist.extend(letter)
    
    # list of wrong guesses 
    st.session_state.wrong_guesses = list(set(st.session_state.letterlist).difference(st.session_state.correctlist))

    st.space(size="medium")

    st.write("Your word looks like this:")


    columsss = st.columns(10)
    for i, col in enumerate(columsss):
        st.markdown("""
        <style>
        .large-snippet {
            font-size: 24px !important;
            font-weight: 500;
            color: #FFF8DC;
        }
        </style>
        """, unsafe_allow_html=True)

        template = Template('<div class="large-snippet"><b>$name</b></div>')
        with col:
          #st.markdown(template.substitute(name=''), unsafe_allow_html=True)
          st.markdown(template.substitute(name='_'), unsafe_allow_html=True)
        
    # display letter if guessed
    if len(st.session_state.letterlist) > 0:
      for index in st.session_state.indiceslist:
        columsss[index].markdown(template.substitute(name=word[index]), unsafe_allow_html=True)

    
    
    
    
    
    
    ## letter lines
    # color palette
    colors = ["#FF4B4B", "#0068C9", "#29B09D", "#FF8700"]

    num_squares = len(word)
    # one square per letter
    inner_squares = "".join([
        f'<div style="width: 57px; height: 5px; background-color:'
        f' {colors[i % len(colors)]}; border-radius: 8px;"></div>'
        for i in range(num_squares)
    ])

    html_squares = f"""
    <div style="display: flex; flex-direction: row; flex-wrap: wrap; gap: 22px; align-items: left;">
        {inner_squares}
    </div>
    """

    # Render the HTML inside st.markdown
    st.markdown(html_squares, unsafe_allow_html=True)

    st.space("medium")

    # discovery if right or wrong guess
    if letter:
      st.write(f"You think '{letter}' is a good choice?")
      time.sleep(3)

      if letter in word and len(letter) == 1 and letter.isalpha() and st.session_state.letterlist.count(letter) == 1:
        st.write(f":green[yay, you are right '{letter}' is part of this word!]")
      elif len(letter) != 1 or not letter.isalpha():
        st.write(f"invalid entry. pls try again :)")
      elif st.session_state.letterlist.count(letter) > 1: 
        st.write(f"you tried '{letter}' before")
      else:
        st.write(f":red[wrooong, sorry '{letter}' is not part of this word.]")


# list of letters already tried
with col3:
    st.write("You already tried:")

    colored_letters = []

    for elements in st.session_state.letterlist:
      if letter in word:
          colored_letters.append(f"**:green[{elements}]**")
      else:
          colored_letters.append(f"**{elements}**")

    s = ", ".join(colored_letters)
    st.markdown(s)




#let ai generate a fitting word 
# save in variable
# animate fitting letter strokes


# if letter in word = yay
# if not = oh no + hangman animation + sound?


# let ai pick a word

# give option to get more background info on word
# - stats

# option for new game 
# clean session state

# abbruchbedingung, wort komplett erraten

# new word 
if st.button("New Game"):
  st.session_state.letterlist.clear()
  st.session_state.correctlist.clear()
  st.session_state.indiceslist.clear()
  st.session_state.wrong_guesses.clear()
  # option for word in same category or different
