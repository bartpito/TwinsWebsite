from textblob import TextBlob

blob = TextBlob("Internet is a great place to learn data science. It helps community through blogs, hackathons, discussions, etc.")

#Tokenization
sent = blob.sentences
words = blob.words

#Part-of-speech tagging
pos = blob.tags
print(pos)


