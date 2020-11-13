from helpers import Pingc
from helpers import Httpc
from helpers import Emailc
from helpers import Sshc
import time

print('starting...')

print('           ____       _           _')
print(' _ __ ___ |  _ \ ___ | |__   ___ | |_')
print('|  _ ` _ \| |_) / _ \|  _ \ / _ \| __|')
print('| | | | | |  _ < (_) | |_) | (_) | |_')
print('|_| |_| |_|_| \_\___/|_.__/ \___/ \__|\n\n')

time.sleep(10)

p1 = Pingc('8.8.8.8')
p1.start_ping()

h1 = Httpc('http://google.com')
h1.start_http_connection()

e1 = Emailc('seiya.ubuntu@gmail.com', 'passwd', 'murilo.oliveira7@hotmail.com')
e1.start_email_send()

s1 = Sshc('M4G0', 'm', 'passwd')
s1.start_ssh_connection()