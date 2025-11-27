import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []
no_l = int(input("How many letters would you want in your password?"))
no_n = int(input("How many numbers would you want in your password?"))
no_s = int(input("How many symbols would you want in your password?"))

for i in range(0, no_l):
    password += random.choice(letters)
for i in range(0, no_n):
    password += random.choice(numbers)
for i in range(0, no_s):
    password += random.choice(symbols)

random.shuffle(password)
final_pass = ""
for i in password:
    final_pass += i

print(f"Random pass is : {final_pass}")


# import random
#
#
# def gen_pass(nr_letters,nr_symbols,nr_numbers):
#     password = []
#     for n in range(0,nr_letters):
#         l = random.choice(letters)
#         password.append(l)
#     for n in range(0,nr_symbols):
#         l = random.choice(symbols)
#         password.append(l)
#     for n in range(0,nr_numbers):
#         l = random.choice(numbers)
#         password.append(l)
#
#     random.shuffle(password)
#     fin_pass = ''
#     for i in password:
#         fin_pass += i
#     return fin_pass
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# n_letters = int(input("How many letters would you like in your password?\n"))
# n_symbols = int(input(f"How many symbols would you like?\n"))
# n_numbers = int(input(f"How many numbers would you like?\n"))
#
# print(f"{gen_pass(n_letters,n_symbols,n_numbers)}")
