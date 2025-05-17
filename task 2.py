import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# 🔧 Force re-download in case of corrupted/missing data
nltk.download('punkt', force=True)
nltk.download('stopwords', force=True)

# Now responses have multiple lines (list of sentences)
responses = {
    'greeting': [
        "Hello! How can I assist you today?\nI hope you're having a great day!",
        "Hi there!\nIt's nice to talk to you. What would you like to chat about?",
        "Hey!\nFeel free to ask me anything or just say hi!"
    ],
    'how_are_you': [
        "I'm doing well, thank you!\nI enjoy chatting with users like you.",
        "Pretty good! Hope you're doing great as well.\nAnything fun planned today?",
        "I am fine, thanks for asking.\nHow about yourself?"
    ],
    'goodbye': [
        "Goodbye!\nHave a wonderful day ahead.",
        "See you later!\nTake care and stay safe.",
        "Take care!\nIt was nice talking to you."
    ],
    'default': [
        "Sorry, I didn't understand that.\nCan you please rephrase or ask something else?",
        "Hmm, I'm not sure I follow.\nCould you try saying it differently?",
        "I'm a bit confused.\nLet's talk about something else!"
    ]
}

keywords = {
    'hello': 'greeting',
    'hi': 'greeting',
    'hey': 'greeting',
    'how': 'how_are_you',
    'you': 'how_are_you',
    'bye': 'goodbye',
    'exit': 'goodbye',
    'quit': 'goodbye'
}

stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [w for w in tokens if w.isalpha() and w not in stop_words]
    return filtered_tokens

def get_intent(user_input):
    tokens = preprocess(user_input)
    for word in tokens:
        if word in keywords:
            return keywords[word]
    return 'default'

def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'quit' or 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print("Chatbot: Goodbye!\nHave a great day!")
            break
        intent = get_intent(user_input)
        reply = random.choice(responses[intent])
        print("Chatbot:", reply, "\n")  # Print multiple lines nicely

if __name__ == "__main__":
    chatbot()
