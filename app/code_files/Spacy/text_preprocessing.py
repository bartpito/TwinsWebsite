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

