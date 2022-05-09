# -*- coding: utf-8 -*-
"""
Created on Mon May  9 08:58:18 2022

@author: Norman
"""

# python script for sending message update

import time
from time import sleep
from sinchsms import SinchSMS

# function for sending SMS
def sendSMS():

	# enter all the details
	# get app_key and app_secret by registering
	# a app on sinchSMS
	number = '5708989654'
	app_key = '873b2e3df44b4cd5bb77baf7c256e95a'
	app_secret = 'b3774120e98f4a93884f0856544bcb93'

	# enter the message to be sent
	message = 'lol, this message was sent from python find all info here: '

	client = SinchSMS(app_key, app_secret)
	print("Sending '%s' to %s" % (message, number))

	response = client.send_message(number, message)
	message_id = response['messageId']
	response = client.check_status(message_id)

	# keep trying unless the status returned is Successful
	while response['status'] != 'Successful':
		print(response['status'])
		time.sleep(1)
		response = client.check_status(message_id)

	print(response['status'])

if __name__ == "__main__":
	sendSMS()
