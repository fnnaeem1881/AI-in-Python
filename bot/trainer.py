from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import joblib
from bot.data import training_data

def train_chatbot_model():
    texts = [data['text'] for data in training_data]
    labels = [data['intent'] for data in training_data]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)

    classifier = SVC(kernel='linear')
    classifier.fit(X, y)

    joblib.dump(classifier, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')

    print("Model training complete. Files saved: model.pkl, vectorizer.pkl, label_encoder.pkl")

def initialize_training():
    print("Re-initializing chatbot training...")
    train_chatbot_model()
