import streamlit as st 
import pandas as pd
from back.sdvBack import concatHOR, concatVER, createGaussian

st.write('Give me a CSV')
dataToEat = st.file_uploader("Upload")
if dataToEat:
    df1 = pd.read_csv(dataToEat)
    df1.drop(df1.columns[df1.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)

st.write("Give me a 2nd CSV")
dataToEat2 = st.file_uploader("Upload 2nd")
if dataToEat2:
    df2 = pd.read_csv(dataToEat2)
    df2.drop(df2.columns[df2.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)

okData = st.button("OK")
if okData:
    """call a function that makes the csv1,synt1,synth2,csv2"""
    """new = pd.concat([df1,df2],axis=0)"""
    """new = concatHOR(df1,df2)"""
    fil1=createGaussian(df2, len(df1))
    fil2=createGaussian(df1, len(df2))
    upData = concatHOR(df1,fil1)
    downData = concatHOR(fil2,df2)
    new = pd.concat([upData, downData],axis=0)
    st.write(new)
    st.write(len(new))