

text_file = open("example.txt", "w")

l=["You","can", "write", "code"]
for item in l:
	
	text_file.write(item+" ")
	#text_file.write(item+"\n")


#print("Opening and closing a file")
#text_file = open("example.txt", "w")
#text_file.write("Goo")

#print (text_file.read().strip("Line"))


text_file.close()
'''

str = "0000000this is string example....wow!!!0000000";
print (str.strip( '0' ))

'''
'''
>>> file=open("example.txt","w")
>>> file.write("Line 1")
6
>>> file.write("Line 2")
6
>>> file.close()
'''