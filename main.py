import streamlit as st

pg = st.navigation([
    st.Page("pages/analysis.py", title="N-Gram Analysis"),
    st.Page("pages/prediction.py", title="Text Prediction")
])

pg.run()