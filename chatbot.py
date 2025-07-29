# ==============================
# 1. Install and Import Libraries
# ==============================
import nltk
import numpy as np
import random
import string  # for punctuation removal
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
#  2. Load and Preprocess WW2.txt
# ==============================
# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load the WW2 text file
with open("WW2.txt", 'r', errors='ignore') as file:
    raw_text = file.read().lower()

# Tokenize the text into sentences
sent_tokens = nltk.sent_tokenize(raw_text)

# ==============================
# 3. Response Generator Function
# ==============================
def response(user_input):
    sent_tokens.append(user_input)
    
    # Vectorize all sentences
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sent_tokens)
    
    # Compute cosine similarity between user input and all sentences
    similarity_scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    idx = similarity_scores.argsort()[0][-1]
    flat = similarity_scores.flatten()
    flat.sort()
    score = flat[-1]

    sent_tokens.pop()  # Clean up user input from sentence list

    if score == 0:
        return "I'm sorry, I didn't understand that."
    else:
        return sent_tokens[idx]

# ==============================
# 4. Chat Loop
# ==============================
print("WW2Bot: Ask me anything about World War II! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    if user_input == 'bye':
        print("WW2Bot: Goodbye!")
        break
    else:
        print("WW2Bot:", response(user_input))
