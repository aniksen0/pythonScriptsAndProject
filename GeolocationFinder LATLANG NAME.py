#Using google API <<Converting Location name to langitude and latitude>>
import requests
# You need to install the requests module to use this code
import json

api_key = False
#don't have API key so i am using your API Key @dr-chuck.thanks.
if api_key is False:
    api_key = 42
    #remember to delete url before push the code <anik>
    serviceurl = 'not included for github'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json'
count=0;
while count<1:
    count+=1
    address = input('Enter location: ')
    if len(address) < 1: break

    payload = dict()
    payload['address'] = address
    if api_key is not False: payload['key'] = api_key

    r = requests.get(serviceurl, params=payload)
    print('Retrieved', r.url)
    data = r.text
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)