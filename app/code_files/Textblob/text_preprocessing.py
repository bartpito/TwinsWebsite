from textblob import TextBlob

blob = TextBlob("Internet is a great place to learn data science. It helps community through blogs, hackathons, discussions, etc.")

#Tokenization
sent = blob.sentences
words = blob.words

#Part-of-speech tagging
pos = blob.tags

#Noun Phrase Extraction
npe = blob.noun_phrases

#Sentiment Analysis
test1 = TextBlob("I hate You")
test2 = TextBlob("I love You")
sentiment1 = test1.sentiment
sentiment2 = test2.sentiment

#Words Inflection and Lemmatization
sentence = TextBlob("Use 4 spaces per indentation level.")
singular = sentence.words.singularize()
plural  = sentence.words.pluralize()

from textblob import Word
w = Word('went')
lemm = w.lemmatize('v') # Pass in WordNet part of speech (verb)

#WordNet Integration
from textblob.wordnet import VERB
word = Word("computer")
synsets_computer =  word.synsets

#You can also create synsets directly.
from textblob.wordnet import Synset
computer = Synset('pc.n.01')
word = Word("computer")
print(computer.synsets)


