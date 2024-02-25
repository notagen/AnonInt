import pandas as pd
import streamlit as st
#SDV Dependencies
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.evaluation.single_table import evaluate_quality
from sdv.evaluation.single_table import get_column_plot


real = st.session_state.template
st.write(real)
metadataButton = st.button('Print Metadata')
if metadataButton:
    metadata = SingleTableMetadata()
    st.session_state.metadata = metadata
    metadata.detect_from_dataframe(real)
    metadata.validate()
    st.write(metadata)



gaussianButton = st.button('Generate Synthetic Gaussian')
if gaussianButton:
    gaussianSynth = GaussianCopulaSynthesizer(st.session_state.metadata)
    gaussianSynth.fit(real)
    synthetic_data_gaussian = gaussianSynth.sample(1000)
    st.write(synthetic_data_gaussian)
    quality_report_gaussian = evaluate_quality(
    real_data=real,
    synthetic_data=synthetic_data_gaussian,
    metadata=st.session_state.metadata)
    st.write(quality_report_gaussian.get_visualization(property_name='Column Shapes'))
    st.write(quality_report_gaussian.get_visualization(property_name='Column Pair Trends'))
    for i in real.columns.tolist():
        fig = get_column_plot(
            real_data=real,
            synthetic_data=synthetic_data_gaussian,
            column_name=i,
            metadata=st.session_state.metadata
        )
        #fig.show()
        st.write(fig)

ctganButton = st.button('Generate Synthetic CTGAN')
if ctganButton:
    ctganSynth = CTGANSynthesizer(st.session_state.metadata)
    ctganSynth.fit(real.sample(300))
    synthetic_data_ctgan = ctganSynth.sample(1000)
    st.write(synthetic_data_ctgan)
    quality_report_ctgan = evaluate_quality(
    real_data=real,
    synthetic_data=synthetic_data_ctgan,
    metadata=st.session_state.metadata)
    st.write(quality_report_ctgan.get_visualization(property_name='Column Shapes'))
    st.write(quality_report_ctgan.get_visualization(property_name='Column Pair Trends'))
    for i in real.columns.tolist():
        fig = get_column_plot(
            real_data=real,
            synthetic_data=synthetic_data_ctgan,
            column_name=i,
            metadata=st.session_state.metadata
        )
        #fig.show()
        st.write(fig)