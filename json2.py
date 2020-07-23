import urllib.request,urllib.parse,urllib.error
import json

address=input('Enter URL: ')
print('Retrieving:', address)
uh=urllib.request.urlopen(address)
data=uh.read().decode()
print('Retrieved',len(data),'characters')

try:
    js=json.loads(data)
except:
    js=None



results=js["comments"]
print('Count: ',len(results))
sum=0
for item in results:
    x=item["count"]
    sum=sum+int(x)
print("Sum:",sum)
