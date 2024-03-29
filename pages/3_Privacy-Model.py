import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
import pyarxaas.privacy_models as pr

st.write("Privacy Models")

attributes = st.session_state.template

if 'modelsList' not in st.session_state:
    st.session_state.modelsList = []


tab1, tab2 = st.columns(2)

with tab1:
    privModel1 = st.selectbox("privacy model for the whole table",("","k-Anonymity"))

    if privModel1 == "k-Anonymity":
        k = st.slider("k", 2, 900, 5, 1)
        privacyModel = pr.KAnonymity(k)
        if st.button("OK"):
            st.session_state.modelsList.append(privacyModel)


 

with tab2:
    chooseAtr4 = st.multiselect("choose attribute to protect", attributes.columns.values.tolist())
    attrDisclosure = st.selectbox("attribute disclosure method", ("", "l-Diversity", "t-Closeness"))
    if attrDisclosure == "l-Diversity":
        l = st.slider("L",2,1000,2,1)
        privacyModel = pr.LDiversityDistinct(l,chooseAtr4[0])
        if st.button("Insert Diversity"):
            st.session_state.modelsList.append(privacyModel)          
    if attrDisclosure == "t-Closeness":
        t_clos = st.slider("t",0.001,1.0,0.001,0.001)
        privacyModel = pr.TClosenessEqualDistance(t_clos)
        if st.button("Inser Closeness"):
            st.session_state.modelsList.append(privacyModel)           


#delete a privacy model
myModels = st.session_state.modelsList
for model in myModels:
    if st.button(str(model)):
        myModels.remove(model)
st.session_state.modelsList = myModels


st.write(st.session_state.dtst.describe)