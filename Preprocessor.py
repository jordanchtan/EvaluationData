import re
import string
import unicodedata
import nltk
# import contractions
import inflect
# from bs4 import BeautifulSoup
# from nltk import word_tokenize, sent_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import LancasterStemmer, WordNetLemmatizer
import pandas as pd
import csv


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    return unicodedata.normalize('NFKD', words).encode(
        'ascii', 'ignore').decode('utf-8', 'ignore')


def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    return words.lower()


def process_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    words = words.strip('"')
    words = re.sub(r'[-]', ' ', words)
    words = re.sub('([.,!?()\'\"])', r' \1 ', words)
    words = re.sub('\s{2,}', ' ', words)
    words = words.strip()
    return words


def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words


def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


def stem_words(words):
    """Stem words in list of tokenized words"""
    stemmer = LancasterStemmer()
    stems = []
    for word in words:
        stem = stemmer.stem(word)
        stems.append(stem)
    return stems


def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
    words = process_punctuation(words)
    # words = replace_numbers(words)
    # words = remove_stopwords(words)

    return words


path = r'.\ReactData\FB_react_data.csv'
df = pd.read_csv(path, encoding='utf16')

df['name'] = df['name'].apply(lambda x: normalize(x))

df.to_csv('pre_FB_react_data.csv', index=False,
          encoding='utf16')
