import requests
import json
def matchingWord(strs):
  link= "https://api.datamuse.com/words"
  param={}
  param["rel_rhy"]=strs
  param['max']=3
  page=requests.get(link, param)
  print(type(page))
  jsonbanalam=page.json()
  return [name['word'] for name in jsonbanalam]

inp=input("input word")
matchingWord(inp)