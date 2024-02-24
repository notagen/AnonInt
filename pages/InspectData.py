import streamlit as st
import pandas as pd
from back.sdvBack import catchDuplicates


tab1, tab2 = st.columns(2)
with tab1:
    st.write('Give me a CSV')
    dataToEat = st.file_uploader("Upload 1")
    if dataToEat:
        df = pd.read_csv(dataToEat)
        df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        st.session_state.dataf1=df
        st.write(df)
        st.write('Data rows:')
        st.write(len(df))
        st.write('Data Columns:')
        st.write(df.columns.tolist())

with tab2:
    st.write('Give me a CSV')
    dataToEat = st.file_uploader("Upload 2")
    if dataToEat:
        df = pd.read_csv(dataToEat)
        df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        st.session_state.dataf2=df
        st.write(df)
        st.write('Data rows:')
        st.write(len(df))
        st.write('Data Columns:')
        st.write(df.columns.tolist())


catch = st.button('Are there any duplicate columns?')
if catch:
    d1 = st.session_state.dataf1
    d2 = st.session_state.dataf2
    duplicate = catchDuplicates(d1, d2)
    st.write(duplicate)
    if len(d1)<len(d2):
        st.write('1 is smaller')
        st.session_state.dataf1 = d1.drop(columns=duplicate)
    else:
        st.write('2 is smaller')
        st.session_state.dataf2 = d2.drop(columns=duplicate)
    st.write('Duplicates has been removed from the smaller dataset')

    