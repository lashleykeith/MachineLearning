from database import Database
from user import User

Database.initialise(database="learning", host="localhost", user="postgres", password="14Lunchtime")

user = User('lashleykeith@gmail.com', 'Keith', 'Lashley', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('lashleykeith@gmail.com')

print(user_from_db)