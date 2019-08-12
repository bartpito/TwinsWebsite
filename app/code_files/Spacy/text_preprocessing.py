import spacy
spacy_nlp = spacy.load('en_core_web_sm')

article = '''In computer science, lexical analysis, lexing or tokenization is the process of 
converting a sequence of characters (such as in a computer program or web page) into a 
sequence of tokens (strings with an assigned and thus identified meaning). A program that 
performs lexical analysis may be termed a lexer, tokenizer,[1] or scanner, though scanner 
is also a term for the first stage of a lexer. A lexer is generally combined with a parser, 
which together analyze the syntax of programming languages, web pages, and so forth.'''

#Processing text with the nlp object returns a Doc object that holds all information about the tokens, their linguistic features and their relationships.
doc = spacy_nlp(article)

#Accessing token attributes
tokens = [token.text for token in doc]

#Accessing spans
span = doc[2:4]

#Creating a span manually
from spacy.tokens import Span

# Span for "New York" with label GPE (geopolitical)
doc = spacy_nlp('I live in New York')
span = Span(doc, 3, 5, label="GPE")

#Attributes return label IDs. For string labels, use the attributes with an underscore. For example, token.pos_.

#Part-of-speech tags
doc = spacy_nlp('this is a text')
pos = [token.pos_ for token in doc]
tag = [token.tag_ for token in doc]

#Syntactic dependencies
dep = [token.dep_ for token in doc]

# Syntactic head token (governor)
head = [token.head.text for token in doc]

#Named Entities
doc = spacy_nlp('Larry Page founded Google')
ne = [(ent.text, ent.label_) for ent in doc.ents]

#Sentences (usually needs the dependency parser)
doc = spacy_nlp('First sentence. Second sentence.')
sents = [sent.text for sent in doc.sents]

#Base noun phrases (needs the tagger and parser)
doc = spacy_nlp('I have a red car and I love football')
chunks = [chunk.text for chunk in doc.noun_chunks]

#Label explanations
#print(spacy.explain('RB'))
#print(spacy.explain('GPE'))

#Visualizing
from spacy import displacy

doc = spacy_nlp('this is a sentence')
#displacy.serve(doc, style='dep')

doc = spacy_nlp('Larry Page founded Google')
#displacy.serve(doc, style='ent')

#To use word vectors, you need to install the larger models ending in md or lg , for example en_core_web_lg.

#Pipeline information
print(spacy_nlp.pipe_names)
print()
print(spacy_nlp.pipeline)