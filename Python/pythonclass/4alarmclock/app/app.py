import time
import webbrowser


total_breaks = 5
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=D93PBlwBp8s")
	break_count = break_count + 1
	print("break count", break_count)


