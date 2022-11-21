import pywhatkit
import time

"""
messages = [
	[number, name]
]
"""

messages = []

message_to_send = lambda x: x



for message in messages:
	number, name = message
	pywhatkit.sendwhatmsg_instantly(number, message_to_send(name), 10, tab_close=True)
	time.sleep(20)
