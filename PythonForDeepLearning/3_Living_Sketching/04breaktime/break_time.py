import time
import webbrowser

total_breaks = 3
break_count = 0
print("This program started on "+time.ctime())
while(break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=D93PBlwBp8s")
	break_count = break_count + 1




	
'''
total_breaks = 3
break_count = 0
input_song = raw_input ("enter your song's url")
print("This program started on "+time.ctime())
while(break_count < total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=D93PBlwBp8s")
	break_count = break_count + 1


play = 0
while (play < 30):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=D93PBlwBp8s")
	play = play + 1
'''	