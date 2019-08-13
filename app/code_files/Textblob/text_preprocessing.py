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
