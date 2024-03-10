import streamlit as st
import pandas as pd
from back.pyarxaasBack import setAttrType
from pyarxaas import Dataset

attributes = st.session_state.template


st.write("Attribute Type")
chooseAtr2 = st.multiselect("choose attribute", attributes.columns.values.tolist())
if chooseAtr2:
    attrType = st.radio("Set attribute type",('Identifying', 'Quasiidentifiyng','Sensitive','Insensitive'))
    if attrType:
        st.write(chooseAtr2[0] + " is " + attrType)
        st.session_state.dtst = setAttrType(chooseAtr2[0], attrType, st.session_state.dtst)

st.write(st.session_state.dtst)