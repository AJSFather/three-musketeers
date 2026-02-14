import re
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, RegexpParser
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
text = load_text('./three-musketeers.txt')
# print(text[:100]) # text loads.

def clean_text(text):
    start_marker = "Title: The three musketeers"
    start_index = text.find(start_marker)
    if start_index != -1:
        text = text[start_index:]
    
    # remove numbers
    text = re.sub(r'\d+', "", text)
    
    # remove special characters
    # text = re.sub(r'[^a-zA-Z0-9\s.]', "", text)
    # remove extra whitespace(s)
    return text

cleaned_text = clean_text(text)
print(cleaned_text[:100])

