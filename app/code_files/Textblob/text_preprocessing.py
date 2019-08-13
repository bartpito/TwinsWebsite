from textblob import TextBlob

blob = TextBlob("Internet is a great place to learn data science. It helps community through blogs, hackathons, discussions, etc .")
sent = blob.sentences
words = blob.words
print(sent)
print("\n\n", words)