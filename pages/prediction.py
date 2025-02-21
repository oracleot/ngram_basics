import streamlit as st
from utils import analyse_ngrams, predict_next_word

st.title("N-Gram Predictive Model")

corpus = st.text_area("Enter your corpus:")
n = st.number_input("Choose N for N-grams (e.g., 2 for bigram, 3 for trigram):", min_value=1, max_value=5, value=2)

if corpus:
    ngram_counts = analyse_ngrams(corpus, n)
    user_input = st.text_input("Enter a word/phrase to predict the next word:")
    
    if user_input:
        st.json(ngram_counts)
        prediction = predict_next_word(ngram_counts, user_input, n)
        # st.write(f"Predicted next word: {prediction}")