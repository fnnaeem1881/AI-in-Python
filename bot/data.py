import json
import os

LOG_FILE = 'logs/conversation_log.json'

# Load the conversation log from file
def load_conversation_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return []

# Save the conversation log to file
def save_conversation_log(conversation_log):
    with open(LOG_FILE, 'w') as f:
        json.dump(conversation_log, f, indent=4)

# Load predefined training data (can be expanded)
def load_default_data():
    return [
        "hello",
        "how are you",
        "goodbye",
        "weather",
        "tell me the weather"
    ], [
        "greeting",
        "greeting",
        "goodbye",
        "weather",
        "weather"
    ]
training_data = [
    {"text": "hi", "intent": "greeting"},
    {"text": "hello", "intent": "greeting"},
    {"text": "hey", "intent": "greeting"},
    {"text": "how are you", "intent": "wellbeing_check"},
    {"text": "how are youy", "intent": "wellbeing_check"},  # Typo variations
    {"text": "what's up", "intent": "wellbeing_check"},
    {"text": "what's your name", "intent": "info"},
    {"text": "tell me your name", "intent": "info"},
    {"text": "who are you", "intent": "info"},
    {"text": "bye", "intent": "farewell"},
    {"text": "goodbye", "intent": "farewell"},
    {"text": "see you", "intent": "farewell"},
]
