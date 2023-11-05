import streamlit as st
import pandas as pd
import numpy as np

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


test_table <- np.array([(1,2,3)],[4,5,6],[7,8,9])

st.table(test_table)

