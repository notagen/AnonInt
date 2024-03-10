import requests
import streamlit as st
import pandas as pd
from pyarxaas import Dataset

url = "http://localhost:8080"
analyseUrl = "http://localhost:8080/api/anonymize"

data = st.session_state.servicePayload

response = requests.post(analyseUrl,json=data)
#df = pd.DataFrame(response.json())
st.write(response.json())
#st.session_state.result = df