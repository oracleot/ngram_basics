from collections import defaultdict
import random

def generate_ngrams(text, n):
    """Generate n-grams from the input text."""
    tokens = text.split()
    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    return ngrams

def build_ngram_model(text, n):
    """Build an n-gram model from the input text."""
    model = defaultdict(list)
    ngrams = generate_ngrams(text, n)
    for gram in ngrams:
        prefix, next_word = gram[:-1], gram[-1]
        model[prefix].append(next_word)
    return model

def generate_text(model, seed, n):
    """Generate a single word using the n-gram model."""
    seed_tokens = seed.split()
    if len(seed_tokens) < n - 1:
        return "cant predict!"
    prefix = tuple(seed_tokens[-(n-1):])  # Ensure the prefix matches the expected n-gram size
    if prefix in model:
        next_word = random.choice(model[prefix])
        return seed + ' ' + next_word
    else:
        return "cant predict!"

corpus = "This is a simple example of an n-gram model in Python. This example shows how it works. a simple illustration is all I have added here. a simple example is occuring again"

# n = 2  # bigram model
# seed = "show"  # Bigram context

n = 3  # trigram model
seed = "a simple"  # Trigram context

# n = 6  # 6-gram model
# seed = "example of an n-gram model"  # 6-gram context
# seed = "example of an n-gram model"  # 6-gram context error!
model = build_ngram_model(corpus, n)

generated_text = generate_text(model, seed, n)
print(generated_text)