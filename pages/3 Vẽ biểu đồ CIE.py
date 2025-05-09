import streamlit as st
import colour
import numpy as np
st.set_page_config(
    page_title="Vẽ biểu đồ CIE", layout="centered")
place = st.empty

figure, axes = colour.plotting.plot_chromaticity_diagram_CIE1931 ()
st.pyplot(figure, clear_figure=True)

