import streamlit as st
import time
from string import Template
import numpy as np
import random

# page layout full screen
st.set_page_config(layout="wide")

# if not provided by page beforehand, result in warning
if "age" not in st.session_state:
    st.session_state.age = ""

# list for all guessed letters/ multiple guessed letters are added multiple times
if "guesslist" not in st.session_state:
    st.session_state.guesslist = []

if "letterlist" not in st.session_state:
    st.session_state.letterlist = []

# list for correct guesses 
if "correctlist" not in st.session_state:
    st.session_state.correctlist = []

# list of correct letter indices
if "indiceslist" not in st.session_state:
    st.session_state.indiceslist = []

# list of wrong guesses
if "wrong_guesses" not in st.session_state:
    st.session_state.wrong_guesses = []

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
game_over = False
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

# randomly choose from these words
if "word" not in st.session_state:
  words = ["apple", "banana", "lemon", "pineapple", "orange"]
  st.session_state.word = random.choice(words)

# guess guessing input over chat bar below with maximum 1 character
guess = ""

# puts input into "guess"
input = st.chat_input("Pick a letter you think is part of this word", max_chars = 1)
if input:
  guess = input.lower()

# add letter to overall guess list
st.session_state.guesslist.extend(guess)

# add valid entries to letter list
if len(guess) == 1 and guess.isalpha and guess not in st.session_state.correctlist:
  st.session_state.letterlist.extend(guess)

# list of indices of correct letters
indices = [i for i, ch in enumerate(st.session_state.word) if ch == guess and i not in st.session_state.indiceslist]
st.session_state.indiceslist.extend(indices)
if guess in st.session_state.word:
  st.session_state.correctlist.extend(guess)

  # game over, won
  if len(st.session_state.correctlist) == len(set(st.session_state.word)):
    game_over = True
    st.session_state.games_won = st.session_state.games_won + 1
    solved = st.session_state.word.upper()
    st.success(f"Juchuuuu, { solved }! You guessed the word correctly!")

    # clear all lists for a new game
    if st.button("New Game"):
      st.switch_page("pages/choose your player.py")
      st.session_state.letterlist.clear()
      st.session_state.correctlist.clear()
      st.session_state.indiceslist.clear()
      st.session_state.wrong_guesses.clear()
      st.session_state.guesslist.clear()
      st.stop
      game_over = False


# list of wrong guesses 
wrong_guesses = list(set(st.session_state.letterlist).difference(st.session_state.correctlist))

# game over, lost
if len(wrong_guesses) > 14:
  game_over = True
  st.session_state.games_lost = st.session_state.games_lost + 1
  st.warning('OH NO, you died :(')

  # start a new game
  if st.button("New Game", on_click=lambda: st.switch_page("pages/choose your player.py")):
      st.session_state.letterlist.clear()
      st.session_state.correctlist.clear()
      st.session_state.indiceslist.clear()
      st.session_state.guesslist.clear()
      wrong_guesses.clear()
      game_over = False


st.space("medium")

if not game_over:
  # horizontal placement of different game parts
  col1, col2, col3 = st.columns([1, 2, 1],wrap=False)

  # visualization of hangman image based on game status
  with col1:
    # start image
    if len(wrong_guesses) == 0:
      link = "happycat.png"
    elif len(wrong_guesses) > 0:
      link = "Hangman" + str(len(wrong_guesses)) + ".jpg"
    st.image(
      link,
      caption="your current closeness level to death",
  )
  with col2:
    #word visualized
    st.write("Your word looks like this:")

    columsss = st.columns(len(st.session_state.word))
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
          st.markdown(template.substitute(name='_'), unsafe_allow_html=True)
        
    # display letter if guessed
    if len(st.session_state.letterlist) > 0: 
      for index in st.session_state.indiceslist:
        columsss[index].markdown(template.substitute(name=st.session_state.word[index]), unsafe_allow_html=True)

 

    st.space("medium")

    # discovery if right or wrong guess
    if guess:
      st.write(f"You think '{guess}' is a good choice?")
      time.sleep(1)

      if guess in st.session_state.word and len(guess) == 1 and guess.isalpha() and st.session_state.guesslist.count(guess) == 1:
        st.write(f":green[yay, you are right '{guess}' is part of this word!]")
      elif len(guess) != 1 or not guess.isalpha():
        st.write(f"invalid entry. please try again :)")
      elif st.session_state.guesslist.count(guess) > 1: 
        st.write(f"you tried '{guess}' before")
      else:
        st.write(f":red[wrooong, sorry '{guess}' is not part of this word.]")


  # list of letters already tried
  with col3:
    st.write("You already tried:")
    st.write(", ".join(st.session_state.guesslist))


  # Restart the game
  if st.button("Restart Game"):
    game_over = True
    st.session_state.letterlist.clear()
    st.session_state.correctlist.clear()
    st.session_state.indiceslist.clear()
    st.session_state.wrong_guesses.clear()
    st.session_state.guesslist.clear()

