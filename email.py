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



print(message)








