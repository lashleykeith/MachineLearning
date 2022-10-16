from user import User


user = User.load_from_file('Guy.txt')

print(user.name)
print(user.movies)