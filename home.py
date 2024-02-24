import streamlit as st
import streamlit.components.v1 as com
import pandas as pd
import datetime
from back.makeTemplates import dictAccess,newTemplate2
#from pyarxaas import ARXaaS
#from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
#from pyarxaas import AttributeType
from pyarxaas import Dataset

df = pd.read_csv("insuranceRoundedBmiClean.csv")
now = datetime.datetime.now()
subDataName = f"data_{now.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
st.session_state.modelsList = []

com.html("<div><h1> this is my interface </h1>")

templs = dictAccess() #{ templName:[], ...}
templateTmp = st.multiselect("Choose template", templs)
if templateTmp:
    st.write(templs[templateTmp[0]]) #templateTemp[0]-->templName, templ[templName]-->list of fields
    #st.write(df[templs[templateTmp[0]]])
    st.session_state.template=df[templs[templateTmp[0]]]
    st.write(st.session_state.template)
    dataset = Dataset.from_pandas(df[templs[templateTmp[0]]])
    st.session_state.dtst = dataset
    if st.button('Save me!'):
        st.session_state.template.to_csv(subDataName, index=False)



st.write("Make a new template")
attributes = pd.read_csv('synthBig.csv')
chooseAtr = st.multiselect("choose columns", attributes.columns.values.tolist())
tmplName = st.text_input("template name")
if st.button("Submit your template"):
    newTemplate2(tmplName, chooseAtr)

#st.write(df)
st.session_state.dtst = Dataset.from_pandas(df)
st.session_state.template = df

