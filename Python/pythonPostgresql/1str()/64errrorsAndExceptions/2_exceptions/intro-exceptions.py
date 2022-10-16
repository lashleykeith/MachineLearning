import requests
from json import JSONDecodeError

"""
number = input("Enter a number: ")
try:
    print(int(number) * 2)
#except ValueError:
except LookupError:
    print("Look up error? This should never happen...")
except ValueError:
    print("You did not enter a base 10 number! Try again.")
print("Hello")
"""

r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON response!")
except KeyError:
    print("We got JSON back from sentiment analysis, but it did not have a key 'label'.")