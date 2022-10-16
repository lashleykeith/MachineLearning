from user import User

my_user = User.load_from_db_by_email('lashleykeith@gmail.com')

print(my_user)

