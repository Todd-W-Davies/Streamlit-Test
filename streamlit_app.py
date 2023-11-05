import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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


df = pd.DataFrame({
  'col1': [1,2,3],
  'col2': [4,5,6],
  'col3': [7,8,9]
})

components.html(df.to_html(header=False, index=False))

