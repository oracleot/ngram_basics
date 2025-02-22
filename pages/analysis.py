import streamlit as st
from utils import get_ngrams_stats

st.title("Corpus Analysis")
st.write("Provide your corpus and select model to visualise word split")

# Text input for the corpus
user_input = st.text_area("Enter the corpus (sentences separated by line breaks):", height=200)

# Define a list of models
models = ["Unigram", "Bigram", "Trigram", "4-gram", "5-gram", "6-gram", "7-gram", "8-gram"]

# N-gram size input
n = st.selectbox("Select a model", models, disabled=not bool(user_input))

if user_input:
    # Split the input text into a list of sentences
    corpus = user_input.split('\n')
    
    # Map the selected model to its corresponding number
    model_number = models.index(n) + 1
    
    # Count n-grams based on the selected model number
    ngram_counts = get_ngrams_stats(corpus, model_number)

    # Prepare data for display with n-gram, count, and percentage
    ngram_data = [{'Word': ' '.join(ngram), 'Count': count, 'Percentage': f"{percentage:.2f}%"} 
                for ngram, count, percentage in ngram_counts]

    # Display the n-grams, their counts, and percentages in a table
    st.table(ngram_data)