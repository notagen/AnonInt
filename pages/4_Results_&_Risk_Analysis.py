import streamlit as st
from pyarxaas import ARXaaS
from pyarxaas.privacy_models import KAnonymity, LDiversityDistinct
from pyarxaas import AttributeType
from pyarxaas import Dataset
import pandas as pd

arxaas = ARXaaS("http://localhost:8080/")



st.write(st.session_state)

if st.button("ANONYMISE"):
    anon_result = arxaas.anonymize(st.session_state.dtst, st.session_state.modelsList)
    st.write(anon_result.dataset.to_dataframe())
    anon_rp = anon_result.risk_profile
    st.write(anon_rp.re_identification_risk)


risk_profile = arxaas.risk_profile(st.session_state.dtst)


st.write(risk_profile.re_identification_risk)



