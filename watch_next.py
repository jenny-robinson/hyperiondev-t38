import spacy

nlp = spacy.load('en_core_web_md')

# open and read movies.txt
file_in = open("movies.txt", "r")
# movie data variable reading all lines in movies.txt
movie_data = file_in.readlines()

# define get_similar_film function
def get_similar_film(description):
    # create variable to tokenise for comparison
    description_token = nlp(description)
    # initialise values for comparison
    highest_similarity = 0
    best_match_movie = ""

    # iterate over movie_data list
    for movie_line in movie_data:
        # remove new lines and split at " :"
        split_data = movie_line.strip("\n").split(" :")

        # check for similarities in descriptions
        token = nlp(split_data[1])

        # returns a float between 0 and 1 describing similarity between 2 tokens
        token_similarity = token.similarity(description_token)

        # conditional statement to check for highest similarity
        if token_similarity > highest_similarity:
            highest_similarity = token_similarity

            # setting movie title
            best_match_movie = split_data[0]

    # print result
    print(f"Best match: {best_match_movie}")

# film description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# call function
get_similar_film(description)