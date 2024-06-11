import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

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


bill_length_mm = st.slider('bill_length_mm', 25,65,40)
bill_depth_mm = st.slider('bill_depth_mm',10,25,18)
flipper_length_mm = st.slider('flipper_length_mm',150,250,200)
body_mass_g = st.slider('body_mass_g',2600,6500,4000)

new_penguin = pd.DataFrame({'bill_length_mm':[bill_length_mm],'bill_depth_mm':[bill_depth_mm],'flipper_length_mm':[flipper_length_mm],'body_mass_g':[body_mass_g]})


st.dataframe(new_penguin)

my_scaler = pickle.load(open('scaler.pickle', 'rb'))
my_kmeans = pickle.load(open('kmeans.pickle', 'rb'))

scaled_new_penguin = my_scaler.transform(new_penguin)
prediction_for_new_penguin = my_kmeans.predict(scaled_new_penguin)
st.write(prediction_for_new_penguin)









          