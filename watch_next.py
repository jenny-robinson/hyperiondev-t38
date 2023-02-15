import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('car bus man wheel ')

# comment about someting