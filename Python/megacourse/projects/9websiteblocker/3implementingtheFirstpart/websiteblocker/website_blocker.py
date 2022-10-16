import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]


print(dt.now())
print(dt(dt.now().year,dt.now().month,dt.now().day,1))
print(dt(dt.now().year,dt.now().month,dt.now().day,2))
while True:
# dt.now() will give you the current date.
	if dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,2):

		print("Working hours...")
		with open(hosts_temp,'r+') as file:
			content=file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+" "+website+"\n")

	else:
		print("Fun hours...")
	time.sleep(5)
	