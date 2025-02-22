import streamlit as st

pg = st.navigation([
    st.Page("pages/analysis.py", title="Corpus Analysis"),
    st.Page("pages/prediction.py", title="Next Word Prediction")
])

pg.run()