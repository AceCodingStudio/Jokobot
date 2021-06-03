import json
import random 

data = json.load(open("jokes.json",))

dic  = random.choice(data)

yn = input("Do you want to hear a joke")
if yn.lower() == "yes":
  
