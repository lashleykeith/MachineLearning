story = '''  Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.

'''

replaced = story.replace("Python","Java")
print(replaced)
wordlist = story.split()
wordfrequency = [wordlist.count(i) for i in wordlist]

print("String\n {} \n".format(story))
print("List \n {} \n".format(str(wordlist)))
print("Frequencies\n {} \n".format(str(wordfrequency)))
print("Match \n {} \n".format(dict(zip(wordlist, wordfrequency))))