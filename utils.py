from collections import Counter
import random
import re

# Load the corpus from a text file
def load_corpus(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]
    
# Clean a sentence by removing non-alphabetic characters and converting to lowercase
def clean(sentence):
    return re.sub(r"[^a-zA-Z\s]", "", sentence).lower()

def analyse_ngrams(corpus, n):
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
    ngram_percentages = [(ngram, count, (count / total_ngrams) * 100) 
                         for ngram, count in ngram_counts.items()]
    
    return ngram_percentages  # List of (ngram, count, percentage) tuples

# Find the most occurring word
def most_occuring_word(ngram_counts):
    if not ngram_counts:  # Check if the list is empty
        return None, 0
    
    # The first item in ngram_counts is the most occurring word since Counter returns sorted counts
    most_common_ngram = max(ngram_counts, key=lambda x: x[1])  # Get the n-gram with the highest count
    
    return most_common_ngram[0][0], most_common_ngram[1]  # Extract the word and its count

def predict_next_word(ngram_counts, input_text, n):
    words = clean(input_text).split()
    
    if len(words) < n - 1:
        return "Please provide more context."
    
    key = tuple(words[-(n-1):])
    possible_next_words = [ngram[-1] for ngram in ngram_counts if ngram[:-1] == key]
    
    if not possible_next_words:
        return "word not found"
    
    return random.choice(possible_next_words)
