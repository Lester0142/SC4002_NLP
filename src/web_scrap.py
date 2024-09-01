import requests
import os
from bs4 import BeautifulSoup
from typing import Tuple

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
    return

def split_text_into_tokens(text: str) -> Tuple[list[str], int]:
    """
    Split text into tokens and count token types
    """
    return

def find_tokens_lemmas(tokens: list[str]):
    """
    Find lemmas of every token in list and count lemma types
    Lemma: remove suffix in words and has to be an actual word
    """
    return 

def find_tokens_stems(tokens: list[str]):
    """
    Find stems of every token in list and count stem types
    Stem: remove suffix in words and need not be an actual word
    """
    return

def stem_token(tokens: list[str]):
    """
    Stem tokens and count number of unique 'stemmed' tokens
    """
    return


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Wikipedia:Subjective_importance"
    print(get_web_text(url=url))
