import spacy

nlp = spacy.load('en_core_web_md')

tokens = nlp('car bus man wheel ')

file_in = open("movies.txt", "r")
movie_data = file_in.readlines()

def get_similar_film(description):
    description_token = nlp(description)
    highest_similarity = 0
    best_match_index = 0
    for pos, movie_line in enumerate(movie_data, 0):
        split_data = movie_line.strip("\n").split(" :")
        token = nlp(split_data[1])
        token_similarity = token.similarity(description_token)
        if token_similarity > highest_similarity:
            highest_similarity = token_similarity
            best_match_index = pos

    movie = movie_data[best_match_index].strip("\n").split(" :")
    print(f"Best match: {movie[0]}")

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
get_similar_film(description)