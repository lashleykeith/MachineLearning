from user import User

my_user = User('aaa@gma.com','Gum','Go', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('lashleykeith@gmail.com')

print(user_from_db)