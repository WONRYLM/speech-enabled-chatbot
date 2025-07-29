# ==========================
# 1. Import Libraries
# ==========================
import streamlit as st
import nltk
import numpy as np
import string
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# ==========================
# 2. Download NLTK Resources
# ==========================
nltk.download('punkt')
nltk.download('wordnet')
nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# ==========================
# 3. Load and Prepare Data
# ==========================
with open("chatbot_data.txt", 'r', encoding='utf8', errors='ignore') as file:
    raw = file.read().lower()

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens if token not in string.punctuation]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# ==========================
# 4. Chatbot Logic
# ==========================
def chatbot_response(user_input):
    sent_tokens.append(user_input)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = np.argsort(vals.flatten())[-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        response = "I'm sorry, I didn't understand that."
    else:
        response = sent_tokens[idx]
    sent_tokens.pop()
    return response

# ==========================
# 5. Speech Recognition
# ==========================
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak into your microphone.")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand your speech."
        except sr.RequestError:
            return "Could not request results; check your network."
        except sr.WaitTimeoutError:
            return "Listening timed out. Please try again."

# ==========================
# 6. Streamlit App
# ==========================
st.set_page_config(page_title="Speech Chatbot", page_icon="")
st.title("Speech-Enabled Chatbot")
st.write("Choose your input method:")

# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

input_method = st.radio("Input Type", ('Text', 'Speech'))

if input_method == 'Text':
    user_input = st.text_input("Type your message here:")
    if st.button("Send") and user_input:
        response = chatbot_response(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

elif input_method == 'Speech':
    if st.button("Start Listening"):
        user_input = transcribe_speech()
        st.write(f"**You said:** {user_input}")
        response = chatbot_response(user_input)
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", response))

# Display chat history
if st.session_state.history:
    st.write("### Chat History:")
    for speaker, message in st.session_state.history:
        st.write(f"**{speaker}:** {message}")
# ==========================