import streamlit as st
import pandas as pd

result = st.session_state.result
elements = result.columns.tolist()

for e in elements:
    st.write(e)
    st.write(result[e])
    for e2 in result[e]:
        st.write(e2)