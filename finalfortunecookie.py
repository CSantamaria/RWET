import sys
import random

jackson = open("Jackson.txt")
jackson_parts = list()

for part in jackson: 
    part = part.strip() 
    jackson_parts.append(part) 
    
random.shuffle(jackson_parts)  
jacksonpart = random.choice(jackson_parts) 
#print jacksonpart

lines_prince = list()     
    
for line in sys.stdin:
	line = line.strip()
	lines_prince.append(line)

random.shuffle(lines_prince)
princepart = random.choice(lines_prince)

print jacksonpart  + "\n"  +  princepart
