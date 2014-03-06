import sys
import random

jackson = open("Jackson.txt")
jackson_parts = list()

for part in jackson: 
    part = part.strip() 
    jackson_parts.append(part) 
    
random.shuffle(jackson_parts) 

lines_prince = list()     
    
for line in sys.stdin:
	line = line.strip()
	lines_prince.append(line)

random.shuffle(lines_prince)

fortune_text = []
for line in lines_prince:
    random.choice(lines_prince)  
    fortune_text.append(line)

for part in jackson_parts:
    random.choice(jackson_parts)
    fortune_text.append(part)

    print fortune_text  
