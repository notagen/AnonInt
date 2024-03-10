import requests
import streamlit as st
import pandas as pd
from pyarxaas import Dataset

url = "http://localhost:8080"
analyseUrl = "http://localhost:8080/api/analyze"
resIndex = ['measures',
'attackerSuccessRate',
'quasiIdentifiers',
'populationModel',
'riskIntervalList',
'quasiIdentifierRiskList']

data = st.session_state.servicePayload

response = requests.post(analyseUrl,json=data)
df = pd.DataFrame(response.json())
st.session_state.result = df

st.write(df)
for col in df:
    for i in resIndex:
        if (col == 'distributionOfRisk' and i == 'riskIntervalList'):
            data = df[col].loc[i]
            riskIn = pd.DataFrame(data)
            st.write(riskIn)
        elif (col == 'attributeRisk' and i == 'quasiIdentifierRiskList'):
            data = df[col].loc[i]
            atrRis = pd.DataFrame(data)
            st.write(atrRis)
        else:
            st.write(df[col].loc[i])