import spacy  # importing spacy


nlp = spacy.load('en_core_web_md')



movies = open("movies.txt", 'r')
movies_contents = movies.read()
list_movie_contents = movies_contents.split("\n")
planet_hulk = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''


def next_movie(description):
    '''
        This function takes in a description of a movie and checks for similarity index
        with other movies, this way it can recommend another movie to watch

        :param str description: This is the movies you've already watched

        :returns: recomendation for next movie to watch

        :rtype: str
    '''
    movie_similar_dict = {}
    movie_to_compare = nlp(description)
    for sentence in list_movie_contents:
        similarity = nlp(sentence[9:]).similarity(movie_to_compare)
        movie_similar_dict[sentence[0:7]] = similarity
    
    return max(movie_similar_dict, key=movie_similar_dict.get)
    

# Call defined function and print out recommended movie title.   
print(f"recommendations: {next_movie(planet_hulk)}")