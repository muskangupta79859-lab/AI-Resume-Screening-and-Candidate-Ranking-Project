import re
import nltk
import spacy
from nltk.corpus import stopwords

# Download NLTK stopwords if missing
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))

# Load spaCy model (download automatically if missing)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download

    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)

    doc = nlp(text)

    cleaned = []

    for token in doc:
        if token.text not in stop_words and not token.is_space:
            cleaned.append(token.lemma_)

    return " ".join(cleaned)