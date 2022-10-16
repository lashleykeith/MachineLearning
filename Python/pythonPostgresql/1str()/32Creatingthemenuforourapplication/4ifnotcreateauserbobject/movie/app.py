import json
import os

from user import User

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

    # Give them a list of options:
    # Add a movie
    # See list of movies
    # Set a movie as watched
    # Delete a movie by name
    # See list of watched movies
    # Save and Quit
    pass

def file_exists(filename):
    return os.path.isfile(filename)

menu()