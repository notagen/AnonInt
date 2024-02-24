import streamlit as st
import pandas as pd
from back.pyarxaasBack import setReductHierarch, setIntervHierarch

attributes = st.session_state.template

st.write("Hierarchies")
chooseAtr3 = st.multiselect("choose attribute to generalize", attributes.columns.values.tolist())
if chooseAtr3:
    st.write('Give me a Hierarchy CSV')
    dataToEat = st.file_uploader("Upload")
    if dataToEat:
        dfHier = pd.read_csv(dataToEat)
        st.session_state.dtst.set_hierarchy(chooseAtr3[0], dfHier)
        st.write(st.session_state.dtst)
    
    
    
    
    
    




            