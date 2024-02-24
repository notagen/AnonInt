import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
import pyarxaas.privacy_models as pr

st.write("Privacy Models")

attributes = st.session_state.template

if 'modelsList' not in st.session_state:
    st.session_state.modelsList = []


tab1, tab2 = st.columns(2)
com.html("""<div><style>
div{
    background-color:DodgerBlue;
}
p{
    background-color:Tomato;
}
</style>""")
with tab1:
    privModel1 = st.selectbox("privacy model for the whole table",("","k-Anonymity","Differental Privacy","δ-Presence","Profitability","Average reidentification risk","Sample Uniquenes"))
    com.html("<p>")
    if privModel1 == "k-Anonymity":
        k = st.slider("k", 2, 900, 5, 1)
        privacyModel = pr.KAnonymity(k)
        if st.button("OK"):
            st.session_state.modelsList.append(privacyModel)
            st.write(st.session_state.modelsList)
    if privModel1 == "δ-Presence":
        x = 0.1
        lowPresence = st.slider("Lower", 0.0, 1.0, x)
        upPresence = st.slider("Upper", 0.0, 1.0, x+0.2)
        if lowPresence>upPresence:
            st.write("low < up !!")
        st.session_state.modelsList.append("2341")
        st.write(st.session_state.modelsList)
    if privModel1 == "Differental Privacy":
        e = st.slider("ε",0.0,10.0,1.0,0.00001)
        d = st.slider("δ",0.0,0.01,0.0,0.00001)
        generalisation = st.selectbox("Generalisation",("","Automatic","None","Low","Medium","High","Complete"))
        if generalisation == "Automatic":
            budget = st.slider("%",0,100,0,1)
    if privModel1 == "Profitability":
        attackerModel = st.selectbox("Attacker Model",("","Journalist","Prosecutor"))
    if privModel1 == "Average reidentification risk":
        thresholdAvg = st.slider("Threshold",0.0,1.0,0.0,0.01)
    if privModel1 == "Sample Uniquenes":
        thresholdSmpl = st.slider("Threshold",0.0,1.0,0.0,0.01)
 

    com.html("</p>")
com.html("</div>")
        

with tab2:
    chooseAtr4 = st.multiselect("choose attribute to protect", attributes.columns.values.tolist())
    attrDisclosure = st.selectbox("attribute disclosure method", ("", "l-Diversity", "δ-Disclosure privacy", "t-Closeness","β-Likeness"))
    if attrDisclosure == "l-Diversity":
        l = st.slider("L",2,1000,2,1)
        variant = st.selectbox("Variant",("","Distinct","Shannon-entropy","Grassbenger-entropy","Recursive(c,l)"))
        if variant == "Recursive(c,l)":
            c_recursive = st.slider("c",0.0001,1000.0,1,0.0001)
    if attrDisclosure == "δ-Disclosure privacy":
        d_disclosure = st.slider("D",1,1000000,4,1)
    if attrDisclosure == "t-Closeness":
        measure = st.selectbox("Measure",("","equal ground distance","hierarchical ground distance","ordered distance"))
        t_clos = st.slider("t",0.001,1.0,0.001,0.001)
    if attrDisclosure == "β-Likeness":
        b_like = st.slider("β",1,1000000,1,1)


st.write(st.session_state.dtst.describe)


""" Στο tab2 θέλει μόνο τα sensitive στη λίστα. Αν δεν έχω τέτοια τότε δε βγάζω τπτ """
""" Θέλω μια λίστα για να κρατάω τα μοντέλα που θα χρησιμοποιηθούν. Αυτη η λίστα μπαίνει ως παράμετρος στο amonymize """