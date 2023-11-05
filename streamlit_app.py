import streamlit as st

st.write("""
# Animal Noises
""")

animal_dict = {
  'cat': 'miaow',
  'cow': 'moo',
  'dog': 'woof',
  'donkey': 'eeyore',
  'duck': 'quack',
  'fish': 'blub',
  'fox': 'ring-ding-ding-ding-dingeringeding',
  'goose': 'honk',
  'horse': 'neigh',
  'mouse': 'squeak',
  'pig': 'oink',
  'sheep': 'baa',
  'snake': 'hiss'
}


animal = st.selectbox(
    'Select an animal',
    list(animal_dict.keys())
)

st.write('The ', animal, ' says ', animal_dict[animal])
