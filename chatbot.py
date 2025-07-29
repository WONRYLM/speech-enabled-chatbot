# ==============================
# 1. Install and Import Libraries
# ==============================
import streamlit as st
import nltk
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# NLTK downloads (run once)
nltk.download('punkt')
nltk.download('wordnet')

# Download punkt tokenizer if not already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
# ==============================
# 2. Load and Preprocess Text
# ==============================
@st.cache_data
def load_text():
    with open("WW2.txt", 'r', errors='ignore') as file:
        raw_text = file.read().lower()
    return nltk.sent_tokenize(raw_text)

sent_tokens = load_text()

# ==============================
# 3. Chatbot Logic
# ==============================
def chatbot_response(user_input):
    sent_tokens.append(user_input)
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sent_tokens)
    similarity_scores = cosine_similarity(tfidf[-1], tfidf[:-1])
    
    idx = similarity_scores.argsort()[0][-1]
    flat = similarity_scores.flatten()
    flat.sort()
    score = flat[-1]
    sent_tokens.pop()
    
    if score == 0:
        return "I'm sorry, I didn't understand that."
    else:
        return sent_tokens[idx]

# ==============================
# 4. Streamlit UI with Chat History
# ==============================
def main():
    st.title("WW2Bot: Ask me about World War II!")
    st.write("Type your question below to learn about World War II from historical text.")

    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User input
    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        if user_input:
            response = chatbot_response(user_input.lower())
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("WW2Bot", response))
        else:
            st.warning("Please enter a question.")

    # Display chat history
    st.markdown("Chat History")
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"** {speaker}:** {message}")
        else:
            st.markdown(f"** {speaker}:** {message}")

if __name__ == '__main__':
    main()
