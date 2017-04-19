#import httplib 
#import urllib2, urllib
import requests
from datetime import datetime, date



id1=5;

dt=datetime.utcnow()
# Formatting datetime
day_time=dt.strftime("%Y%m%d %H:%M:%S")

headers1 = {
    'Content-type': 'application/x-www-form-urlencoded',
}

data1 = {
    'Description': 'Errore con data e ora corretti',
    'IdType': '6',
    'IdApparato': id1,
    'DateTime' : day_time
}



url2 = "http://40.68.169.138/Narvalo/NarvaloWS/api/Narvalo/AddDiagnostica"
#req2 = urllib2.Request(url2, data, headers)
#r2 = urllib2.urlopen(req2)
#print r2.read()




 
#url = "url to contact"
#cookies1 = {'cookie1_name': 'cookie_value', 'cookie1_name': 'cookie_value'}
#data1= {'username': username, 'password': current_pass}
r = requests.post(url2, data=data1, headers=headers1)

result = r.text
print result
