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
    # If it already exists, welcome them and load their data.
    # If not, create a User object.

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