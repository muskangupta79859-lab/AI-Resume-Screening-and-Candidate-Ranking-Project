import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if missing
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", " ", text)

    words = text.split()

    cleaned = [
        word
        for word in words
        if word not in stop_words and len(word) > 1
    ]

    return " ".join(cleaned)