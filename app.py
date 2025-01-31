# for loop

bot_names = ["Jeff", "Paul", "Chris"]
for name in bot_names:
    print(name)

# while loop
  
name = "Jeff"
while name == "Jeff":
    print(name)
    name = "Francis"
    print(name)

 # function and import
from datetime import datetime

def add_numbers(a,b):
    return a + b

#print(add_numbers(3,5))

def get_todays_date():
    return datetime.now().strftime("%m/%d/%Y")

print(get_todays_date())