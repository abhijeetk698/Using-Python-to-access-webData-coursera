import urllib
from urllib import request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_328590.html';
html=urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print(sum)
