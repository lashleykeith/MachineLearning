import time
from datetime import datetime as dt

host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
# dt.now() will give you the current date.
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):

		print("Working hours...")
	else:
		print("Fun hours...")
	time.sleep(5)
	