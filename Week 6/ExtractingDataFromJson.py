import json
import urllib
from urllib import request
count = 0
sum = 0
url = input("Enter Url - ")

data = urllib.request.urlopen(url).read().decode()

info = json.loads(str(data))
for i in info['comments']:
    count = count+1
    sum = sum + i['count']

print("Sum : ",sum)
