import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("\n======= cat, monkey, banana example =======")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat and monkey are the most similar at nearly 0.6
# cat and banana are the least similar at 0.22
# banana and monkey are more similar than banana and cat 
# despite being a fruit and an animal also
# but, monkeys do eat bananas!

word1 = nlp("bus")
word2 = nlp("train")
word3 = nlp("driver")

print("\n======= bus, train, driver own example =======")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# when using 'en_core_web_sm', a lot of information is displayed
# for example:
# print(word1.similarity(word2))
# 0.6770565478895127
# /Users/jenny/Dropbox/JM22100004702/Software Engineer Bootcamp/T38/semantic.py:11: 
# UserWarning: [W007] The model you're using has no word vectors loaded, 
# so the result of the Doc.similarity method will be based on the tagger, 
# parser and NER, which may not give useful similarity judgements. 
# This may happen if you're using one of the small models, 
# e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
# You can always add your own word vectors, or use one of the larger models instead if available.
# 'en_core_web_md' is more concise

tokens = nlp('car bus man wheel ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))