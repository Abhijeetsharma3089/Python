import random

print("Welcome we will provide you random passwords")

char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+123456789"

number=int(input("Amount of passwords to be generated : "))

length=int(input("Input your password length : "))

print("\n here is your lists of passwords")

for passwd in range(number):
    passwords=''
    for password in range(length):
        passwords += random.choices(char)
    print(passwords)