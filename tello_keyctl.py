from tello import Tello
import sys
from datetime import datetime
import time
import re

from sys import stdin,stdout
print("Hello")

tello = Tello()
tello.send_command("command")
time.sleep(3)
print("Enter key: t(takeoff),l(land) or q(quit)")
for l in stdin:
	print(l)
	c=l.strip()
	if re.search('t',c):
		command="takeoff\r\n"	
	if re.search('l',c):
		command="land\r\n"
	if re.search('u',c):
		command="up 50\r\n"
	if re.search('d',c):
		command="down 50\r\n"
	if re.search('p',c):
		command="right 30\r\n"
	if re.search('d',c):
		command="right 30\r\n"
	if re.search('a',c):
		command="left 30\r\n"
	if re.search('w',c):
		command="forward 30\r\n"
	if re.search('s',c):
		command="back 30"
	if re.search('q',c):
		print("land and exit")
		tello.send_command("land\r\n")
		sys.exit(0)
	print(command)
	response=tello.send_command(command)
	print(response)
	time.sleep(0.5)
