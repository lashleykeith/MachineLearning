# Ask for the user's name.
# Check if a file exists for that user.
# If it already exists, welcome them and load their data.
# If not, create a User object.

# Give them a list of options:
# Add a movie
# See list of movies
# Set a movie as watched
# Delete a movie by name
# See list of watched movies
# Save and Quit
import json
import os

from user import User
def menu():
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 'v' to see the list of movies," 
                      "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                      ", 's' to save or 'q' to quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 'v':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(movie.name,movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif user_input == 's':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                       "or q to save and quiz")


def file_exists(filename):
    return os.path.isfile(filename)

menu()