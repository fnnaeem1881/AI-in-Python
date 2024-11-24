import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

# Initialize the model components
vectorizer = TfidfVectorizer()
classifier = MultinomialNB()
label_encoder = LabelEncoder()

# Load model if exists, else return empty components
def load_model():
    try:
        classifier = joblib.load('model.pkl')
        vectorizer = joblib.load('vectorizer.pkl')
        label_encoder = joblib.load('label_encoder.pkl')
        
        # Ensure the vectorizer is fitted
        if not hasattr(vectorizer, 'vocabulary_'):
            vectorizer.fit([""])  # Fit with an empty string or some sample data

        return classifier, vectorizer, label_encoder
    except FileNotFoundError:
        # If the model files don't exist, return the default components
        return classifier, vectorizer, label_encoder

# Save the model after updating it
def save_model():
    joblib.dump(classifier, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')
