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
from operator import itemgetter 
#import nltk 
#print (time.strftime("%H:%M:%S"))

moment = int(time.strftime("%H"))

api_key = sys.argv[1]
 
feelings = open('feelings.txt', 'r')
feelings_words = []

words = open('WORDS.txt', 'r')
all_words = [] 

meaning = []
meaningfeeling = []
wordsmeaning = []



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
url = "http://api.wordnik.com/v4/word.json/" + urllib.quote_plus(am.strip()) + \
    "/definitions?" + urllib.urlencode(params)
    
    
#print url
urlobj = urllib.urlopen(url)
result = json.loads(urlobj.read())
#print result
definition = result 



if moment <9:
#if len(result) > 0:
 for definition in result:
    #print definition
    print definition['text'] 

elif moment >=9 and moment <=17:
    #print result[0]["text"]
    output = []
    for definition in result: 
        meaning = definition["text"].split()#.extend(definition['text'].strip().split(' '))
        for short in meaning:
            #short = itemgetter(random.randint(1,2))(meaning)
            output.append(short)

            #sliceSizer = 4 #random.randint(0, moment)/8
            sliceSize = (random.randint(0,moment),random.randint(0,moment))
            sliceToJoin = output.append(pm[0])

            #initialText[n:sliceSize]



            
            #if sliceSizer < moment:
                #output.append(pm[0])
          
    #print output
    print " ".join(output)#*random.randint(0,moment/4)

else:
    print pm 
