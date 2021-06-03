import json
import random 
import time

data = json.load(open("jokes.json",))

dic  = random.choice(data)

yn = input("Do you want to hear a joke")
if yn.lower() == "yes":
  print(dic["setup"])
  time.sleep(3)
  print(dic["punchline"])
else:
  print("sorry man, i am going then )
  
