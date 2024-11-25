import random

letters = ["A","B","C","D","E","F","a","b","c","d","e","f"]
symbols = ["!","@","#","$","%","&","*"]
numbers = [1,2,3,4,5,6,7,8,9,0]
password = []


user_letter = int(input("Letters?"))
user_symbols = int(input("Symbols?"))
user_numbers = int(input("Numbers?"))

# My Logic

for i in range(0,user_letter):
    # print(letters[i])
    password.append(letters[random.randint(0,11)])

for i in range(0,user_symbols):
    # print(symbols[i])
    password.append(symbols[random.randint(0,6)])

for i in range (0,user_numbers):
    # print(numbers[i])
    password.append(numbers[random.randint(0,9)])

print("Your Generated 2 Passwords are: ")
print(password)
for i in password:
    print(i,end='')

print(end='\n')

#shuffle password to make new one

random.shuffle(password)
print(password)
for i in password:
    print(i,end='')

#You can also print the items by making a string(so that you can store your password)
# instead of only printing list items
#take an empty string iterate through your password list and add each item in your empty string

#password_string = ''
#for i in password:
#   password_string += i
#print(password_string)



# Angela Logic

# I'm just writing it try it your self

# Instead of array take string
# password = ''

# Instead of randint use choice cuz it's made to pick random item from list
# password += random.choice(letters)


