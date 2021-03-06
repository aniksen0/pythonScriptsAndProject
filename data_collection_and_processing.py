# -*- coding: utf-8 -*-
"""Data collection and processing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bpcjX0K61H4QaOpNC7hMVJbV7LZ0SDca
"""

import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested.keys():
    data=True
else:
    data=False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour=False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole'in nested.values():
  print(True)
else:
  print(False)
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

print(nested_d.keys())
for p_id, p_info in nested_d.items():
    US_count.append(p_info['USA'])

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
if 'data' in nested.keys():
    data=True
else:
    data=False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
if 24 in nested.keys():
    twentyfour=True
else:
    twentyfour=False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
if 'whole'in nested.values():
    whole=True
else:
    whole=False
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
if 'physics' in nested.keys():
    physics=True
else:
    physics=False

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
print(nested_d.keys())
print(nested_d['London']['Great Britain'])

"""**WEEK 2 (Python classes and inheritance)**

"""

def a(b):
  return b==5

a(5)

def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))

t='hello'
s=t*2
print(s)

#list com
ll = [value for value in range(53)]
print(ll)

#Below, we have provided a list of lists that contain information about people.
#Write code to create a new list that contains every person’s last name, and save that list as last_names.


info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_name=[]
for idx in info:
  last_name.append(idx[1])

print(last_name)

#Counting string len without len function
str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
count=0
for i in str1:
  count+=1
print(count)

#upper using MAP fuction
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
w="w"
abbrevs_upper = map(lambda item:item.upper(), abbrevs)
new = filter(lambda name:'w' in name, abbrevs)

print(list(new))
print(list(abbrevs_upper))

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
w=lst_check[0]

new = filter(lambda name: w in name, lst_check)

print(list(new))

"""Adding two list using zip and list comprehension

"""

L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = [x1+x2 for (x1, x2) in list(zip(L1, L2))]
print(L3)

#zip and list compres using with if statement
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1 + x2 for (x1, x2) in list(zip(L1, L2))if(x1>10 and x2 < 5)]
print(L3)

def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))

#list comprehension tupple second name finding

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names=[idx[1] for idx in people]

#doubling the value using list comprehension. 

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

lst2=[value*2 for value in lst]

#passed in for and if condition using list comp
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed=[name for name, value in students if value>=70]

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info=zip(species, population)

endangered = [name for name,value in pop_info if value<2500]

#using map adding new string on list;

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing=map(lambda name: "Fruit: " +name, lst_check)
print(list(map_testing))

#using zip and list comprehension (matrices addition)<if condition
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1+x2 for (x1, x2) in list(zip(L1, L2)) if (x1>10) and (x2<5)]
print(L3)

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
endangered=[]
pop_info=zip(species,population)
for x1,x2 in pop_info:
    if x2<2500:
        endangered.append(x1)

"""**REST API** Learning from -21.8.2020

"""

import requests
import json
def matchingWord(strs):
  link= "https://api.datamuse.com/words"
  param={}
  param["rel_rhy"]=strs
  param['max']=10
  page=requests.get(link, param)
  print(type(page))
  jsonbanalam=page.json()
  return [name['word'] for name in jsonbanalam]

inp=input("input word")
matchingWord(inp)

import requests
import json

def abar(word):
  url='https://api.datamuse.com/words'
  param={}
  param['rel_rhy']=word
  param['max']=4
  page=requests.get(url,param)
  load=page.json()
  return [dic['word'] for dic in load]

abar("funny")

#Creating Requests with cache .

import requests
import json

PERMANENT_CACHE_FNAME = "permanent_cache.txt"
TEMP_CACHE_FNAME = "this_page_cache.txt"

def _write_to_file(cache, fname):
    with open(fname, 'w') as outfile:
        outfile.write(json.dumps(cache, indent=2))

def _read_from_file(fname):
    try:
        with open(fname, 'r') as infile:
            res = infile.read()
            return json.loads(res)
    except:
        return {}

def add_to_cache(cache_file, cache_key, cache_value):
    temp_cache = _read_from_file(cache_file)
    temp_cache[cache_key] = cache_value
    _write_to_file(temp_cache, cache_file)

def clear_cache(cache_file=TEMP_CACHE_FNAME):
    _write_to_file({}, cache_file)

def make_cache_key(baseurl, params_d, private_keys=["api_key"]):
    """Makes a long string representing the query.
    Alphabetize the keys from the params dictionary so we get the same order each time.
    Omit keys with private info."""
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)

def get(baseurl, params={}, private_keys_to_ignore=["api_key"], permanent_cache_file=PERMANENT_CACHE_FNAME, temp_cache_file=TEMP_CACHE_FNAME):
    full_url = requests.requestURL(baseurl, params)
    cache_key = make_cache_key(baseurl, params, private_keys_to_ignore)
    # Load the permanent and page-specific caches from files
    permanent_cache = _read_from_file(permanent_cache_file)
    temp_cache = _read_from_file(temp_cache_file)
    if cache_key in temp_cache:
        print("found in temp_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(temp_cache[cache_key], full_url)
    elif cache_key in permanent_cache:
        print("found in permanent_cache")
        # make a Response object containing text from the change, and the full_url that would have been fetched
        return requests.Response(permanent_cache[cache_key], full_url)
    else:
        print("new; adding to cache")
        # actually request it
        resp = requests.get(baseurl, params)
        # save it
        add_to_cache(temp_cache_file, cache_key, resp.text)
        return resp

# import statements
import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    print(flickr_resp.url) # Paste the result into the browser to check it out...
    return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)

#Using google API <<Converting Location name to langitude and latitude>>
import requests
# You need to install the requests module to use this code
import json

api_key = False
# If you have a Google Places API key, enter it here
#api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json'
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

import json
import requests


def get_movies_from_tastedive(name):
    url="https://tastedive.com/api/similar"
    param={}
    param['q']=name
    param['type']='movies'
    param['limit']=5
    response=requests.get(url,params=param)
    return response.json()

def extract_movie_titles(word):
    mvname=[]
    print(word)
    list1=word['Similar']['Results']
    print(list1)
    for idx in list1:
        mvname.append(idx['Name'])
    return mvname
def get_related_titles(inputli):
    listmovie=[]
    for i in inputli:
        newlist=extract_movie_titles(get_movies_from_tastedive(i))
        for j in newlist:
            if j not in listmovie:
                listmovie.append(j)
    return listmovie

import json
import requests

def get_movie_data(title):

    base="http://www.omdbapi.com/"

    d={}

    d['t']=title

    d['r']='json'

    dicto=requests.get(base,params=d)

    return dicto.json()
def get_movie_rating(st):
    rating=st['Ratings']
    for idx in rating:
        if idx['Source']=="Rotten Tomatoes":
            a=idx['Value'].strip('%')
            return int(a)
    return 0

get_movie_data("titan")

import pyautogui
import time
while True:
  time.sleep(4)
  pyautogui.typewrite("happy birthday haramjada")
  pyautogui.press('enter')

"""##### CLASS AND INSTANCE ######

"""

class piglet:
  name ="bolod"
  def speak(self):
    print("hello my name {} i speak oink!".format(self.name))


hamlet=piglet()
hamlet.name="anik"
hamlet.speak()

class animal:
    def __init__(self,arms,legs):
        self.arms=arms
        self.legs=legs
        
    def spidlimbs(self):
        limbs=self.arms+self.legs
        return limbs
    
    

spider=animal(4,4)
print(spider.spidlimbs())

class Cereal:
    def __init__(self,name,brand,fiber):
        self.name=name
        self.brand=brand
        self.fiber=fiber
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)
    
    
     
c1=Cereal("Corn Flakes","Kellogg's" ,2)
print(c1)
c2=Cereal("Honey Nut Cheerios","General Mills",3)

class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()



play()

class Bike():
    def __init__(self,color,price):
        self.color=color
        self.price=price
        
testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)

class AppleBasket():
    def __init__(self,color,apple_quantity):
        self.color=color
        self.apple_quantity=apple_quantity
    def increase(self):
        self.apple_quantity+=1
    def __str__(self):
        return 'A basket of {0} {1} apples.'.format(self.apple_quantity,self.color)

class BankAccount():
    def __init__(self, name, amt):
        self.name=name
        self.amt=amt
    def __str__(self):
        return "Your account, {0}, has {1} dollars.".format(self.name,self.amt)
    
    
t1=BankAccount("Bob",100)

ll1=[1,2,3,5,6,7,8]
find=8
leng=len(ll1)
print(leng)
first=0
last=leng-1
mid=int((first+last)/2)
print(mid)
print(ll1[mid])
while True:
  if ll1[mid]==find:
    print("found at index {}".format(mid))
    break
  elif ll1[mid]<find:
    first=mid+1
    mid=int((first+last)/2)

  elif ll1[mid]>find:
    last=mid-1
    mid=int(first+last/2)
  else:
    print("not found")

for i in range(0,1):
  w=str(i)
  pyautogui.typewrite(w.zfill(4))
  print("try {}".format(i))
  pyautogui.press('enter')
  pyautogui.press('enter')

"""**TRY AND EXCEPT**"""

gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
        
    except:
        country_gold.append("Did not get gold")


print(countr)

#Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except:
        continue

print("Total number of puppies:", total)

#The list, numb, contains integers. Write code that populates the list remainder with the remainder of 36 divided by each number in numb. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string “Error” appear in the remainder.

numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []
for i in numb:
    try:
        remainder.append(36%i)
    except:
        remainder.append("Error")

