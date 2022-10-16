from user import User

user = User("Him")

user.add_movie("The Matrix", "Sci-Fi")
user.add_movie("The Interview", "Comedy")

user.save_to_file()
