import re
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, RegexpParser
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
text = load_text('./three-musketeers.txt')
# print(text[:100])


