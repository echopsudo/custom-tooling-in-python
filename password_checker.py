
print("password strength checker")

password = "Ttest123~"
score = 0
strong_chars = "!@#$%^&*()_+-={}][~`!?"


#password length is the stength measurer

def special_cases(password):
    strength = 0
    for chars in strong_chars:
        if chars in password:
            strength += 4
    for letter in password:
        if letter.isupper():
            strength += 2
        elif letter.isnumeric():
            strength += 1
    return strength

score += len(password) + special_cases(password)

if score >= 25:
    print("very strong")
elif score >= 20:
    print("strong")
elif score >= 15:
    print("moderate")
elif score >= 10:
    print("weak")
elif score >= 5:
    print("very weak")
else:
    print("this password is too weak, try again")
