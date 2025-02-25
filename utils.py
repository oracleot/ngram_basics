from collections import Counter
import random
import re

# Load the corpus from a text file
def load_corpus(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]
    
# Split the text into sentences
def split_into_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)
    
# Clean a sentence by removing non-alphabetic characters and converting to lowercase
def clean(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()

# Analyse the n-grams in the corpus and return the statistics
def get_ngrams_stats(corpus, n):
    ngrams = []  # This will store the n-grams
    all_words = []  # This will hold all words from the corpus in order

    # Process each sentence in the corpus
    for sentence in corpus:
        words = clean(sentence).split()  # Convert to lowercase and split into words
        all_words.extend(words)  # Add all words to the continuous list
    
    # Generate n-grams by sliding a window of size n over the entire word list
    for i in range(len(all_words) - n + 1):
        ngram = tuple(all_words[i:i + n])  # Create the n-gram as a tuple
        ngrams.append(ngram)
    
    # Count the occurrences of each n-gram
    ngram_counts = Counter(ngrams)
    
    # Calculate the total number of n-grams
    total_ngrams = sum(ngram_counts.values())
    
    # Create a list of tuples: (ngram, count, percentage)
    ngram_stats = [(ngram, count, (count / total_ngrams) * 100) 
                   for ngram, count in ngram_counts.items()]
    
    # Sort the list by count in descending order
    ngram_stats = sorted(ngram_stats, key=lambda x: x[1], reverse=True)
    
    return ngram_stats

# Analyse the n-grams in the corpus and return the counts
def get_ngrams_count(corpus, n):
    ngrams = []
    all_words = []
    
    for sentence in corpus:
        words = clean(sentence).split()  # Split into words after cleaning
        all_words.extend(words)
    
    for i in range(len(all_words) - n + 1):
        ngram = tuple(all_words[i:i + n])
        ngrams.append(ngram)
    
    ngram_counts = Counter(ngrams)
    
    return ngram_counts  # Return only the counts for efficiency

# Find the most occurring word
def most_occuring_word(ngram_counts):
    if not ngram_counts:  # Check if the list is empty
        return None, 0
    
    # The first item in ngram_counts is the most occurring word since Counter returns sorted counts
    most_common_ngram = max(ngram_counts, key=lambda x: x[1])  # Get the n-gram with the highest count
    
    return most_common_ngram[0][0], most_common_ngram[1]  # Extract the word and its count

# Predict the next word based on the context
def predict_next_word(corpus, phrase, n):
    ngram_counts = get_ngrams_count(corpus, n)
    words = clean(phrase).split()
    
    if len(words) < n - 1:
        return "gibberish"  # Not enough words to form a valid context
    
    context = tuple(words[-(n-1):])  # Get the last (n-1) words as context
    candidates = {}

    # Iterate through ngram_counts to find matches with context
    for ngram, count in ngram_counts.items():
        if ngram[:-1] == context:  # Compare the first (n-1) words of the n-gram with context
            candidates[ngram[-1]] = count
    
    if not candidates:
        return "gibberish"
    
    # Find the word with the highest frequency
    max_freq = max(candidates.values())
    top_choices = [word for word, freq in candidates.items() if freq == max_freq]
    
    return random.choice(top_choices) if len(top_choices) > 1 else top_choices[0]

def total_words_len(corpus):
    return sum(len(clean(sentence).split()) for sentence in corpus)
