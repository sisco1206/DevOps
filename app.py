# for loop

'''bot_names = ["Jeff", "Paul", "Chris"]
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

print(get_todays_date())'''

# my first chatbot
from datetime import datetime

name = "jeff"

def add(a, b):
    return a + b

def get_todays_date():
    return datetime.now().strftime("%m/%d/%Y")

while True:
    user_message = input("Bot - How can I help you today? ").strip().lower()

    if user_message == "what is your name?":
        print("Bot - My name is", name)

    elif user_message == "what is the date?":
        print("Bot - Today's date is", get_todays_date())

    elif user_message == "exit":
        print("Bot - Goodbye!")
        break  # Exits the loop

    else:
        print("Bot - I'm sorry, I don't understand that.")