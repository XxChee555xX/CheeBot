import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import re

anottext = """This is a really really really kinda long sentence that I was to lazy to extend,Except for that Jeff is a pudding, he was known for being scary,
                  who knew that this would happened?Ben was the only one who knew,however he did now do well to prevent this,Ken then left the Rift.I don't even have any
                   idea what i'm doing."""

def Stem(text) :
    ps = PorterStemmer()
    text = re.split('\s',text)
    for w in text:
        return ps.stem(w)


def Lemmanize(text):
    Lem = WordNetLemmatizer()
    return Lem.lemmatize(text)

def Tokenize(text):
    words = nltk.word_tokenize(text)
    return  words

def StopWordRemoval(text):
    stop_words = set(stopwords.words('english'))
    SimText = [w for w in word_tokenize(text) if not w in stop_words]
    return SimText

def Tag(text):
    if type(text) is not list :
        text = Tokenize(text)
    tagged = nltk.pos_tag(text)
    return tagged

def NaEnRe(text):
    if type(text) is not list:
        text = Tokenize(text)
    namedEnt = nltk.ne_chunk(text)
    return namedEnt


def Define(text):
    z = wordnet.synsets(text)
    meanings = ''
    for w in z:
        meanings += (w.definition()+'; ')
    return meanings

def Nyms(text):
    synonyms = []
    antonyms = []
    for nyms in wordnet.synsets(text):
        for nym in nyms.lemmas():
            if nym.name() not in synonyms:
                synonyms.append(nym.name())
            if nym.antonyms():
                if nym.antonyms() not in antonyms:
                    antonyms.append(nym.antonyms()[0].name())

    for syn in synonyms:
        print(syn)
    for ant in antonyms:
        print(ant)

def Classify(text):
    documents = []
    pass


