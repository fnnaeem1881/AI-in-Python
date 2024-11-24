from bot.model import load_model

classifier, vectorizer, label_encoder = load_model()

import re

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation and extra spaces
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def generate_response(user_input):
    user_input = preprocess_text(user_input)
    intent = predict_intent(user_input)

    responses = {
        "greeting": ["Hello!", "Hi there!", "Hey!"],
        "farewell": ["Goodbye!", "See you later!", "Take care!"],
        "wellbeing_check": ["I'm just a bot, but I'm doing great!", "Thanks for asking! How can I help you?"],
        "info": ["I'm a chatbot created to assist you.", "I can answer your questions and have basic conversations!"],
    }

    from random import choice
    if intent in responses:
        return choice(responses[intent])
    else:
        return "I'm sorry, I didn't understand that. Could you rephrase?"

def predict_intent(user_input):
    X = vectorizer.transform([user_input])
    y = classifier.predict(X)
    return label_encoder.inverse_transform(y)[0]
