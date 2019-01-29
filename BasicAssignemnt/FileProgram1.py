"""

import os
user_input = raw_input("Enter name: ")
user_input1 = raw_input('Enter case: ')
path1 = user_input
if not os.path.exists(path1):
    os.makedirs(path1)

"""
#Directoryname=input("Enter directory name:")
import os.path
import os
import smtplib
import zipfile
import tempfile
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

dirname  = raw_input("enter the dir name:")

pathname = dirname
print pathname

if os.path.isdir(pathname):
    os.makedirs(pathname)

setdirectory = os.chdir(pathname)

print setdirectory
print (os.getcwd())

if os.path.isdir(dir) and len(os.listdir(dir)) == 0:
    print "Empty"


"""
input_file = input("Enter File name : ")
file_txt = open(input_file)
filename = raw_input("Enter File name:")
fname = setdirectory + '/' + filename + '.txt'
temp_file = open(fname, 'w')
    
for dirname, subdirs, files in os.walk("pathname"):
    print dirname
    print subdirs
    print files
"""


