import streamlit as st
from utils import predict_next_word, split_into_sentences

st.title("Next Word Prediction")

corpus = st.text_area("Enter your corpus:")
n = st.number_input("Choose N for N-grams (e.g., 2 for bigram, 3 for trigram):", min_value=1, max_value=5, value=2)

if corpus:
    user_input = st.text_input("Enter a word/phrase to predict the next word:")
    
    if user_input:
        prediction = predict_next_word(split_into_sentences(corpus), user_input, n)
        st.subheader(f"\"{prediction}\"")