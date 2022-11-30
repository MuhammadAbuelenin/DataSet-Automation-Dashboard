import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Data Analysis')
st.subheader('Data Analysis using Python & Streamlit')

upload = st.file_uploader('Upload Your Dataset (In CSV Format)')

if upload is not None:
    data = pd.read_csv(upload)


if upload is not None:
    if st.checkbox('Preview Dataset'):
        head = st.button('Show first 5 Rows')
        tail = st.button('Show last 5 Rows')
        if head:
            st.write(data.head())
        if tail:
            st.write(data.tail())

if upload is not None:
    if st.checkbox('Preview Data Shape'):
        shape = st.radio('Which Dim would you like to check?', ('Rows', 'Columns'))
        if shape == 'Rows':
            st.text('Number of Rows')
            st.write(data.shape[0])
        if shape == 'Columns':
            st.text('Number of Columns')
            st.write(data.shape[1])

if upload is not None:
    test = data.isna().values.any()
    if test:
        if st.checkbox('Check Null Values in DataSet'):
            st.write(data.isna().any())
        else:
            st.success('Congratulation!! No missing values')


if upload is not None:
    if st.checkbox('Check Duplicate Values'):
        st.text('Duplicated Values :')
        no_of_dup = st.write(data.duplicated().sum())
        st.write(data.loc[data.duplicated()])
        if no_of_dup != 0:
            drop_values = st.button('Drop Values')
            if drop_values:
                data = data.drop_duplicates()
                st.text('Now Drop Data equal : ')
                st.write(data.duplicated().sum())


if upload is not None:
    if st.checkbox('Cehck Overview Statistics'):
        data = data.drop_duplicates()
        st.write(data.describe())

if upload is not None:
    data = data.drop_duplicates()
    st.text('Showing a Plot for Selected Column')
    column = st.selectbox('Select a column :-', data.columns)
    sns.countplot(data[column])
    plt.xticks(rotation=45)
    st.pyplot()
    plt.show()

if upload is not None:
    if st.button('About App'):
        st.text('Built by Streamlit')
        st.text('Thank you, Muhammad Abuelenin')
