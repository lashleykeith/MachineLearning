from movies import Movie
from user import User
user = User("Cups")

my_movie = Movie("The  Matrix", "Sci-Fi")

user.movies.append(my_movie)

print(user)
print(user.movies)