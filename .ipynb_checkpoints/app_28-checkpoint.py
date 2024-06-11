import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Our app is amazing :sunglasses:')

st.text('Whatever')

peng_df = sns.load_dataset('penguins')

with st.expander('Click here if you want to see the penguins dataset'):
    st.dataframe(peng_df)

col1, col2, col3 = st.columns(3)

with col1:
    st.image('Images/Adelie.png',caption='Adelie penguin')
with col2:
    st.image('Images/Chinstrap.png',caption='Chinstrap penguin')
with col3:
    st.image('Images/Gentoo.png',caption='Gentoo penguin')