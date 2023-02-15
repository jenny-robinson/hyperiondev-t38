import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('car bus man wheel ')

# comment about someting
file_in = open("movies.txt", "r")

data = file_in.readlines()

# loop over each line of data
for pos, line in enumerate(data, 0):
    print(line)