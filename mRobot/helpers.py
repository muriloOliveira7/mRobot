from pythonping import ping
import urllib.request
import random

class Pingc:
    def __init__(self, ip):
        self.ip = ip

    def start_ping(self):
        print('mRobot will ping ' + self.ip)
        ping(self.ip, count=random.randint(1, 73), verbose=True)

class Http_connection:
    def __init__(self, http_url):
        self.http_url = http_url

    def start_http_connection(self):
        print('mRobot will access ' + self.http_url)

        resp = 0  # initiate variable
        headers = {}  # variable to recieve the web browser header
        headers[
            'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"  # url that will be acessed
        req = urllib.request.Request(self.http_url, headers=headers)  # request to the server using the header
        resp = urllib.request.urlopen(req)  # acess the url using the request above

        if resp != 0:  # Check if the URL was acessed
            print(url, " was acessed!!!")