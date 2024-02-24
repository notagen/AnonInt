import pandas as pd
import streamlit as st
#SDV Dependencies
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
from sdv.single_table import GaussianCopulaSynthesizer


real = st.session_state.template

st.write(real)
metadataButton = st.button('Print Metadata')
if metadataButton:
    metadata = SingleTableMetadata()
    st.session_state.metadata = metadata
    metadata.detect_from_dataframe(real)
    metadata.validate()
    st.write(metadata)

gaussianButton = st.button('Generate Synthetic')
if gaussianButton:
    ctganSynth = CTGANSynthesizer(st.session_state.metadata)
    ctganSynth.fit(real)
    synthetic_data_ctgan = ctganSynth.sample(100)
    st.write(synthetic_data_ctgan)