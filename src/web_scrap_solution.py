import urllib.request 
import nltk
from bs4 import BeautifulSoup
import nltk.stem.porter 

with urllib.request.urlopen("https://en.wilkipedia.org/wiki/Natural_language_processing") as response: 
    html=response.read()

text = BeautifulSoup(html, "lxml").get_text()

sentences = nltk.tokenize.sent_tokenize(text)
print ("Number of sentences: " + str(len(sentences)))

tokens= nltk.tokenize.word_tokenize(text)
print ("Number of tokens: " + str(len(tokens)))

token_types = list(set(tokens))
print ("Number of token types: " + str(len(token_types)))

wnl=nltk.stem.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()
lemma_types= set()
stemmed_types= set()

for token_type in token_types:
    lemma_types.add(wnl.lemmatize(token_type))
    stemmed_types.add(stemmer.stem(token_type))

print ("Number of lemma types: " + str(len (lemma_types)))
print ("Number of stemmed types: " + str(len(stemmed_types)))