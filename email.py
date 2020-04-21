#!/usr/bin/env python3
#
#   S
#   s
#   s
#
#   Author:     Sandro Aguilar
#   Date:       April 20, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
from email.message import EmailMessage

sender = "aguilarsunny@yahoo.com"
recipient = "vluedevil@yahoo.com"

message = EmailMessage()

message['From'] = sender
message['To'] = recipient

message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = "Hey there! I'm learning to send emails using Python!"

message.set_content(body)

print(message)








