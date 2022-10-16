from movie import Movie

class User:
    def __init__(self,name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre): # my_user_object.add_movie()
        movie = Movie(name,genre, False)
        self.movies.append(movie)

    def delete_mov(self, name, genre):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))


    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name,movie.genre,str(movie.watched)))