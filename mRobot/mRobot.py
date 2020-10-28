from helpers import Pingc
from helpers import Http_connection

p1 = Pingc("8.8.8.8")
#p1.start_ping()

h1 = Http_connection('http://google.com')
#h1.start_http_connection()
