import streamlit as st
import pandas as pd
from back.sdvBack import concatHOR, concatVER


df1 = st.session_state.dataf1
df2 = st.session_state.dataf2

tab1, tab2 = st.columns(2)
with tab1:
    st.write(df1)
with tab2:
    st.write(df2)
    

okDataV = st.button("Merge Vertically")
if okDataV:
    new = concatVER(df1,df2)
    st.write(new)
    st.write(len(new))

okDataH = st.button("Merge Horizontally")
if okDataH:
    new = concatHOR(df1, df2)
    st.write(new)
    st.write(len(new))

