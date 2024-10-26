import random

count=1
while True:
    print("Help")
    if random.choice(range(1000))==111:
        break
    print("Let me out")
    count+=1

print("at last it takes",count," tries to escape")    
