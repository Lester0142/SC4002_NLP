import requests
import os
from bs4 import BeautifulSoup
from typing import Tuple
import nltk

def get_web_text(url: os.PathLike) -> str:
    """
    Get text from url using requests and beautiful soup.
    """
    # Send an HTTP request to the URL of the webpage you want to access
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract the text content of the webpage
    text = soup.get_text()
    return text

def split_text_into_sentences(text: str) -> Tuple[list[str], int]:
    """
    Split text into sentences and count number of sentences
    """
    sentences = nltk.tokenize.sent_tokenize(text)
    return sentences, len(sentences)

def split_text_into_tokens(text: str) -> Tuple[list[str], int]:
    """
    Split text into tokens and count token types
    """
    tokens = nltk.tokenize.word_tokenize(text)
    token_types = list(set(tokens))
    return token_types, len(token_types)

def find_tokens_lemmas(token_types: list[str]) -> Tuple[set, int]:
    """
    Find lemmas of every token in list and count lemma types
    Lemma: remove suffix in words and has to be an actual word
    """
    lemmatized = set()
    wnl = nltk.stem.WordNetLemmatizer()
    for token_type in token_types:
        lemmatized.add(wnl.lemmatize(token_type))
    return list(lemmatized), len(lemmatized)

def find_tokens_stems(token_types: list[str]) -> Tuple[set, int]:
    """
    Find stems of every token in list and count stem types
    Stem: remove suffix in words and need not be an actual word
    """
    stemmed = set()
    stemmer = nltk.stem.porter.PorterStemmer()
    for token_type in token_types:
        stemmed.add(stemmer.stem(token_type))
    return list(stemmed), len(stemmed)

if __name__ == "__main__":
    # Web Scrap
    url = "https://en.wilkipedia.org/wiki/Natural_language_processing"
    text = get_web_text(url=url)
    print(text)
    # Split for Sentences
    sentences = split_text_into_sentences(text)
    print ("Number of sentences: " + str(sentences[1]))
    # Split for Tokens
    tokens = split_text_into_tokens(text)
    print ("Number of tokens: " + str(tokens[1]))
    # lemmatize Tokens
    lem_tokens = find_tokens_lemmas(tokens[0])
    print ("Number of lemma types: " + str(lem_tokens[1]))
    # stem Tokens
    stem_tokens = find_tokens_stems(tokens[0])
    print ("Number of stemmed types: " + str(stem_tokens[1]))


