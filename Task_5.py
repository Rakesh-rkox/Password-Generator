
# Max Function: Using for Loop to Find the Maximum Score
student_scores = [150, 142, 135, 160, 155, 148, 170, 165, 140, 175]

# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(f"New maximum score found: {max_score}")

#Range Function: 
# for number in range(1, 10, 4):
#     print(number)

#Gauss Challenge: Using for Loop to Find the Sum of Numbers from 1 to 100
# total = 0
# for number in range(1, 101):
#     total += number
    
# print(f"Sum of numbers from 1 to 100: {total}")

#FizzBuzz Challenge: Using for Loop to Print Numbers from 1 to 100 with FizzBuzz Logic
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

#Password Generator Challenge: Using for Loop to Generate a Random Password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the Password Generator!")
import random
py_letters = int(input("How many letters would you like in your password?\n"))
py_symbols = int(input("How many symbols would you like?\n"))
py_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for i in range(0, py_letters):
    letter = random.choice(letters)
    password_list.append(letter)

for i in range(0, py_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)

for i in range(0, py_numbers):
    number = random.choice(numbers)
    password_list.append(number)

print(password_list)
random.shuffle(password_list)
print(f"Your generated password is: {password_list}")

password = ""
for char in password_list:
    password += char 

print(f"Your final password is: {password}")