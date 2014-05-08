#*** In the inside there is sleeping, in the outside there is reddening,***#
#*** in the morning there is meaning, in the evening there is feeling.***# 
#*** In the evening there is feeling. ***# 

import re
import sys
import random
import urllib
import json
from random import choice 
import time
#print (time.strftime("%H:%M:%S"))

moment = int(time.strftime("%H"))

api_key = sys.argv[1]
 
feelings = open('feelings.txt', 'r')
feelings_words = []

words = open('WORDS.txt', 'r')
all_words = [] 

meaning = []

meaningfeeling = []



for feeling in feelings: 
    feeling = feeling.strip()
    word = feeling.split()
    feelings_words.append(word)
    pm = random.choice(feelings_words)    
   
for word in words: 
   #word = word.strip()
   #english = word.split()
    all_words.extend(word.strip().split(' '))
    all_words.append(word)
    #random.shuffle(all_words)
    am = random.choice(all_words)
    
params = {
     'limit': 1,
     'includeRelated': 'false',
     'api_key': api_key
}
url = "http://api.wordnik.com/v4/word.json/" + urllib.quote_plus(am) + \
    "/definitions?" + urllib.urlencode(params)
    
    
#print url

urlobj = urllib.urlopen(url)
result = json.loads(urlobj.read())
#print result

display = " " 

if moment < 8:
#if len(result) > 0:
  for definition in result:
    #print definition
    print definition['text']

elif moment >=8 and moment <=16:
  for definition in result:
    if len(definition) < 2:
      print 
      #meaning = word.split('')
      
      for i in range(len(meaning) - 1): 
        newmeaning= meaning[i:i+random(1,3)].join(pm)
        meaningfeeling.append(newmeaning) 
        
        print meaningfeeling
      
        #mf = random.choice(meaning)
    #print definition
       #print definition['text']
   
 
else:
      print pm  #Sometimes it prints, but sometimes it doesn't and actually gets stuck in the same word. Over and over.
   
        
