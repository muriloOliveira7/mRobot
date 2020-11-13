import time
import random
from pythonping import ping
import urllib.request
import smtplib
import paramiko
import os

class Pingc: # Ping Class to generate ICMP traffic
    def __init__(self, ip):
        self.ip = ip # ip or url to ping

    def start_ping(self):
        print('mRobot will ping ' + self.ip)
        time.sleep(random.randint(3, 12)) # script will wait between 3 and 12 seconds
        ping(self.ip, count=random.randint(1, 73), verbose=True) # ping function will ping between 5 and 73 times the ip
        print('mRobot has finished the ping\n') # Print confirmation

class Httpc: #HTTP Class to generate HTTP traffic
    def __init__(self, http_url):
        self.http_url = http_url # url that will be acessed

    def start_http_connection(self):
        print('mRobot will access ' + self.http_url)
        time.sleep(random.randint(3, 12)) # script will wait between 3 and 12 seconds

        resp = 0  # initiate variable
        headers = {}  # variable to recieve the web browser header
        headers[
            'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"  # browser header
        req = urllib.request.Request(self.http_url, headers=headers)  # request to the server using the header
        resp = urllib.request.urlopen(req)  # acess the url using the request above

        if resp != 0:  # Check if the URL was acessed
            print(self.http_url + " was accessed!\n") # Print confirmation

class Emailc:
    def __init__(self, semail, spasswd, remail):
        self.semail = semail # Sender of the message
        self.spasswd = spasswd # Sender password
        self.remail = remail # Receiver of the message

    def start_email_send(self):
        print('mRobot will send an email to ' + self.remail)
        time.sleep(random.randint(3, 12))  # script will wait between 3 and 12 seconds

        server = smtplib.SMTP('smtp.gmail.com', 587)  # SMTP configuration of the server
        server.starttls()  # Setting the encryption protocol
        server.login(self.semail, self.spasswd)  # Login to the server

        localtime = time.asctime(time.localtime(time.time())) # Getting formatted time

        message_body = This email was sent from a python code on ' # Message that will be sent
        message_body = message_body + localtime
        server.sendmail(self.semail, self.remail, message_body)  # Sending the message
        print(self.remail + ' received an email\n')  # Print confirmation
        server.quit()  # Close connection

class Sshc:
    def __init__(self, ip, user, passwd):
        self.ip = ip # IP of the ssh server
        self.user = user # User of the ssh server
        self.passwd = passwd # User's password of the ssh server

    def start_ssh_connection(self):
        print('mRobot will ssh to ' + self.ip)
        time.sleep(random.randint(3, 12))  # script will wait between 3 and 12 seconds

        session = paramiko.SSHClient()  # Importing the function
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept any new host connection

        session.connect(self.ip, username=self.user, password=self.passwd)  # Openning connection

        # Commands
        stdin, stdout, stderr = session.exec_command('ls', 'lsls')
        lines = stdout.readlines()
        print(lines)

        session.close()  # Closing connection

    def start_ssh_connection_mcommands(self):
        print('mRobot will ssh to ' + self.ip)
        time.sleep(random.randint(3, 12))  # script will wait between 3 and 12 seconds

        session = paramiko.SSHClient()  # Importing the function
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Accept any new host connection

        session.connect(self.ip, username=self.user, password=self.passwd)  # Openning connection

        channel = session.invoke_shell()
        stdin = channel.makefile('wb')
        stdout = channel.makefile('rb')

        # Commands
        stdin.write('''
        cd /home/m/Documents/
        mkdir python_access
        cd python_access
        date >> access_log
        exit
        ''')
        print (stdout.read())

        stdout.close()
        stdin.close()
        session.close() # Closing connection

        print (self.ip + ' session was closed') # Print confirmation