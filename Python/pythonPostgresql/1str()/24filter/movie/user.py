class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

        #Calculate a list of movies that have been watched
        #You want to initialize an empty list
        # Then iterate over self.movies
        # if the movie.watched is true, add it to the list
        # Return the list


    # def watched_movies(self):
    #     watched_movies_list = []
    #     for movie in self.movies:
    #         if movie.watched:
    #             watched_movies_list.append(movie)
    #     return watched_movies_list


    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched