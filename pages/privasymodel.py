import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
import pyarxaas.privacy_models as pr

st.write("Privacy Models")

attributes = st.session_state.template

if 'modelsList' not in st.session_state:
    st.session_state.modelsList = []

tab1, tab2 = st.columns(2)
com.html("<div><style>div{background-color:DodgerBlue;}p{background-color:Tomato;}</style>")
with tab1:
    privModel1 = st.selectbox("privacy model for the whole table",("","k-Anonymity"))
    com.html("<p>")
    if privModel1 == "k-Anonymity":
        k = st.slider("k", 2, 900, 5, 1)
        privacyModel = pr.KAnonymity(k)
        if st.button("Insert Model"):
            st.session_state.modelsList.append({
            "privacyModel" : "KANONYMITY",
            "params" : {
            "k" : k}
            })
    com.html("</p>")
com.html("</div>")
i=0      

with tab2:
    chooseAtr4 = st.multiselect("choose attribute to protect", attributes.columns.values.tolist())
    attrDisclosure = st.selectbox("attribute disclosure method", ("", "l-Diversity", "t-Closeness"))
    if attrDisclosure == "l-Diversity":
        l = st.slider("L",2,1000,2,1)
        if st.button("Insert Attribute Model"):
            st.session_state.modelsList.append({
            "privacyModel" : "LDIVERSITY_DISTINCT",
            "params" : {
            "column_name" : chooseAtr4[0],
            "l" : l}
            })
    if attrDisclosure == "t-Closeness":
        measure = st.selectbox("Measure",("","equal ground distance","hierarchical ground distance","ordered distance"))
        t_clos = st.slider("t",0.001,1.0,0.001,0.001)

#delete a privacy model
myModels = st.session_state.modelsList
for model in myModels:
    if st.button(str(model)):
        myModels.remove(model)


myDict = st.session_state.dtst._payload()
myDict.update({"privacyModels": st.session_state.modelsList, "suppressionLimit":0.02})
st.session_state.servicePayload = myDict

if st.button("Show Privacy Models"):
    st.write(st.session_state.servicePayload)
st.write(i)

