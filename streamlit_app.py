import streamlit as st

st.write("""
# My first app
Animal Noises
""")

animal_dict = {
  'cat': 'miaow',
  'cow': 'moo',
  'dog': 'woof',
  'duck': 'quack',
  'fish': 'blub',
  'horse': 'neigh',
  'pig': 'oink'
}


animal = st.selectbox(
    'Select an animal',
    list(animal_dict.keys())
)
