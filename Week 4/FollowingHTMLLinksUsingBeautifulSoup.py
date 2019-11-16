import urllib
from urllib import request
from bs4 import BeautifulSoup
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")
    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(s[position-1])
    print (t[position-1])
    url = s[position-1]
