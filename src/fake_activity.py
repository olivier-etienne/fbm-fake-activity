from fbchat import Client
from fbchat.models import *
from random import randint
import os
import time
import datetime


fb_login = os.environ("fb_login")
fb_passwd = os.environ("fb_passwd")

while True:
	client = Client(fb_login, fb_passwd)

	users = client.searchForUsers("mark zuckerberg")
	threads = client.fetchThreadList(limit = 10)

	now = datetime.datetime.now()
	if (now.hour > 1) or (now.hour < 7):
		sleep_time = randint(40, 120) * 60
	else:
		sleep_time = randint(5, 10) * 60

	print ("Sleeping " + str(sleep_time))
	time.sleep(sleep_time)
