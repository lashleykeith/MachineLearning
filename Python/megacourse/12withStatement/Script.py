with open("example.txt", "a+") as f:
	f.seek(0)
	content=f.read()
	f.write("Hi ")
print(content)


