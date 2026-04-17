import random

print("password generator")

real_name = input("What's your real name?: ")
fav_number = input("What's your favourite number?: ")
location = input("Where are you from?: ")
birthyear = input("What is your birthyear?: ")
fav_color = input("What's your favourite color?: ")

choices = [real_name, fav_number, location, birthyear, fav_color]
length = random.randrange(2, 6)

def generate_username():
    result = ""
    for times in range(length):
        random_choice = choices.pop(random.randrange(len(choices)))
        result += random_choice

    print(result)

generate_username()
