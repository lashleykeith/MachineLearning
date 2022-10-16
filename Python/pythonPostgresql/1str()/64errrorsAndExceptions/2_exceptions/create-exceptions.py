class MissingLabelError(KeyError):
    pass

class PageNotFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass

# Program... user enters wrong username
def login():
    raise IncorrectUsernameError

try:
    login()
except IncorrectUsernameError:
    print("You username was incorrect.  Have you forgotten it?")
except IncorrectPasswordError:
    print("Your password was wrong. Have you forgotten it?")