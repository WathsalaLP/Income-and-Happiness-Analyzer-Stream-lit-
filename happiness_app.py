import streamlit as st
import pandas as pd
import numpy as np


#Add Sidebar
st.sidebar.header('User Input')
st.sidebar.text('First enter your name')

#Text Input
user_name=st.sidebar.text_input('Enter your name:')

#Add button
btn_click= st.sidebar.button("Submit")

#print name
if btn_click:
    st.write(f"Hello, {user_name}!")


#Title
st.title('Income Data Analyse')

#Upload income.data.csv file
uploaded_file= 'income.data.csv'

#Load data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
data_load_state = st.text('loading data')
data = load_data(uploaded_file)
data_load_state.text("DONE!!")

#Inspecting Data
st.subheader('Inspecting Data')
st.write('Column in the dataset :', data.columns)
st.write(data.head())

#Add column name to dataset
#column_names= data.columns.to_list()


#upload media
st.sidebar.header('Upload and Display Media')
uploaded_media=st.sidebar.file_uploader("Choose a file:", type=['jpg','jpeg','png','mp4','mp3'])

if uploaded_media is not None:
    if uploaded_media.type.startswith("image"):
        st.image(uploaded_media)
    elif uploaded_media.type=="video/mp4":
        st.video(uploaded_media)
    elif uploaded_media.type=="audio/mp3":
        st.audio(uploaded_media)

#Add progress bar
progress_bar=st.progress(0)
for present_complete in range(10):
    progress_bar.progress(present_complete+1)

#draw histogram
st.subheader("Histogram of Income")
income_values = np.histogram(data['income'],bins=499)[0]
st.bar_chart(income_values)

st.subheader("Histogram of Happiness")
happiness_values = np.histogram(data['happiness'],bins=499)[0]
st.bar_chart(happiness_values)

#show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#comment
comment=st.text_input('Comment:')

#Add submit button
btn_submit2= st.button("SUBMIT")

#print name
if btn_submit2:
    st.write(f"Thank you for your comment!")


